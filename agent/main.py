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
from agent.settings import settings

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

app = FastAPI(title="agent-home")


class ChatRequest(BaseModel):
    message: str


def sse(event: str, payload: dict) -> str:
    """Format one SSE frame. Payloads are JSON so newlines cannot break framing."""
    return f"event: {event}\ndata: {json.dumps(payload)}\n\n"


async def stream_chat(message: str) -> AsyncIterator[str]:
    """Translate the Strands event stream into SSE frames.

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
    agent = build_agent()
    in_flight: dict[str, tuple[str, float]] = {}

    async for event in agent.stream_async(message):
        if "data" in event:
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

    yield sse("done", {})


@app.post("/chat")
async def chat(
    request: ChatRequest,
    x_user_id: Annotated[str | None, Header()] = None,
) -> StreamingResponse:
    # Open WebUI's user ID, sent by the Pipe. Logged only — it becomes the Honcho
    # peer ID in stage 4.
    logger.info("chat request from user %s", x_user_id)
    return StreamingResponse(
        stream_chat(request.message),
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
