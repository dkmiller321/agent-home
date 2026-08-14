"""FastAPI service wrapping the Strands agent."""

import json
import logging
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

    Tool use arrives as a partial-input chunk per delta, so tool calls are
    de-duplicated on toolUseId and announced once, when first seen.
    """
    agent = build_agent()
    announced_tool_uses: set[str | None] = set()

    async for event in agent.stream_async(message):
        if "data" in event:
            yield sse("token", {"text": event["data"]})
            continue

        tool_use = event.get("current_tool_use")
        if tool_use and tool_use.get("toolUseId") not in announced_tool_uses:
            announced_tool_uses.add(tool_use.get("toolUseId"))
            logger.info("tool call: %s", tool_use.get("name"))
            yield sse("tool", {"name": tool_use.get("name")})

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
