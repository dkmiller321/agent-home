"""FastAPI service wrapping the Strands agent."""

import json
import logging
import time
from collections.abc import AsyncIterator
from typing import Annotated

from fastapi import FastAPI, Header
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from agent.agent import build_agent
from agent.memory import load_context, record_turn
from agent.settings import settings

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

app = FastAPI(title="agent-home")


class ChatRequest(BaseModel):
    message: str


def sse(event: str, payload: dict) -> str:
    """Format one SSE frame. Payloads are JSON so newlines cannot break framing."""
    return f"event: {event}\ndata: {json.dumps(payload)}\n\n"


async def stream_chat(message: str, peer_id: str, session_id: str) -> AsyncIterator[str]:
    """Translate the Strands event stream into SSE frames.

    Memory brackets the stream: context is read before the agent is built,
    because it goes into the system prompt, and the turn is written after the
    last token, because the reply does not exist until then. The write is
    awaited rather than left running — it is one request, and losing a turn
    silently because the response finished first would be worse than the wait.

    Tool boundaries come from the two message events, not from
    `current_tool_use`: that one arrives once per input delta carrying a
    half-built JSON string, so it can say a tool is starting but not which URL
    it is fetching. The assistant message lands with inputs already parsed, and
    always before any tool runs.

    `ToolResultEvent` looks like the obvious finish signal and is not one — it
    sets `is_callback_event` to False, and `stream_async` only yields callback
    events. The user-role message carrying `toolResult` blocks is what actually
    arrives.
    """
    agent = build_agent(peer_id, await load_context(peer_id))
    in_flight: dict[str, tuple[str, float]] = {}
    reply: list[str] = []

    async for event in agent.stream_async(message):
        if "data" in event:
            reply.append(event["data"])
            yield sse("token", {"text": event["data"]})
            continue

        message_event = event.get("message")
        if not message_event:
            continue

        for block in message_event.get("content", []):
            if tool_use := block.get("toolUse"):
                tool_use_id, name = tool_use["toolUseId"], tool_use["name"]
                in_flight[tool_use_id] = (name, time.monotonic())
                logger.info("tool start: %s %s", name, tool_use.get("input"))
                yield sse(
                    "tool_start",
                    {"id": tool_use_id, "name": name, "input": tool_use.get("input")},
                )

            elif tool_result := block.get("toolResult"):
                tool_use_id = tool_result["toolUseId"]
                # Absent only if a result arrives for a tool we never announced.
                name, started_at = in_flight.pop(tool_use_id, ("unknown", time.monotonic()))
                status = tool_result.get("status", "success")
                seconds = round(time.monotonic() - started_at, 1)
                logger.info("tool end: %s %s in %ss", name, status, seconds)
                yield sse(
                    "tool_end",
                    {"id": tool_use_id, "name": name, "status": status, "seconds": seconds},
                )

    await record_turn(peer_id, session_id, message, "".join(reply))
    yield sse("done", {})


@app.post("/chat")
async def chat(
    request: ChatRequest,
    x_user_id: Annotated[str, Header()],
    x_session_id: Annotated[str, Header()],
) -> StreamingResponse:
    """Run one turn. Both headers are required, hence no defaults.

    x_user_id is Open WebUI's user ID and becomes the Honcho peer ID verbatim;
    x_session_id is its chat ID. Guessing either would file a turn under the
    wrong person or the wrong conversation, so a missing header is a 422 rather
    than something we paper over.
    """
    logger.info("chat request from user %s in session %s", x_user_id, x_session_id)
    return StreamingResponse(
        stream_chat(request.message, x_user_id, x_session_id),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.agent_host,
        port=settings.agent_port,
        log_level=settings.log_level.lower(),
    )
