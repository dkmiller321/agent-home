"""
title: Agent Home
author: agent-home
version: 0.1.0
description: Thin client for the agent service. Streams /chat back to the browser.
"""

# Installed by pasting this file into Admin Settings -> Functions in Open WebUI.
# It runs inside the Open WebUI container, so it imports only from that image and
# never from agent/ — the two do not share a process or a virtualenv.
#
# Everything it does: forward the latest user message to /chat, turn the SSE
# frames that come back into the string chunks Open WebUI streams to the browser,
# and render tool activity as status events. Agent behavior belongs on the other
# side of that HTTP call; only the wording of the status line is decided here.
#
# Status events specifically, not message/replace: under native tool calling
# Open WebUI overwrites the message body with completion snapshots, so anything
# written that way disappears. Status lines live above the message and survive.

import json
import os
from collections.abc import AsyncIterator

import aiohttp
from pydantic import BaseModel, Field


async def sse_frames(response: aiohttp.ClientResponse) -> AsyncIterator[tuple[str, dict]]:
    """Yield (event, payload) pairs from an SSE response.

    The agent writes one `event:` line and one JSON `data:` line per frame, so a
    frame is complete as soon as its data line arrives. Payloads are JSON, which
    is why a token containing newlines still occupies a single line here.
    """
    event = None
    async for raw_line in response.content:
        line = raw_line.decode().strip()
        if line.startswith("event: "):
            event = line.removeprefix("event: ")
        elif line.startswith("data: ") and event is not None:
            yield event, json.loads(line.removeprefix("data: "))
            event = None


def describe_call(name: str, tool_input: dict | None) -> str:
    """Render a tool call as one short line, e.g. `web_fetch(https://example.com)`.

    Values only: argument names are noise at a glance, and the interesting one is
    almost always first.
    """
    if not tool_input:
        return f"{name}()"
    joined = ", ".join(str(value) for value in tool_input.values())
    if len(joined) > 60:
        joined = f"{joined[:57]}..."
    return f"{name}({joined})"


class Pipe:
    class Valves(BaseModel):
        AGENT_SERVICE_URL: str = Field(
            default=os.getenv("AGENT_SERVICE_URL", "http://agent:8080"),
            description=(
                "Base URL of the agent service. Under Compose this is the service "
                "name. If the agent runs on the host during development, use "
                "http://host.docker.internal:8080"
            ),
        )

    def __init__(self):
        self.valves = self.Valves()

    def pipes(self) -> list[dict]:
        return [{"id": "agent-home", "name": "Agent Home"}]

    async def pipe(
        self,
        body: dict,
        __user__: dict,
        __metadata__: dict,
        __event_emitter__,
    ) -> AsyncIterator[str]:
        """Stream one turn.

        Open WebUI's user and chat IDs go across as headers and become the
        Honcho peer and session IDs unchanged — memory is keyed on identity the
        UI already has, so there is nothing to generate here. Both are required
        by the agent, which answers 422 without them.
        """
        message = body["messages"][-1]["content"]

        async def status(description: str, done: bool) -> None:
            await __event_emitter__(
                {"type": "status", "data": {"description": description, "done": done}}
            )

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.valves.AGENT_SERVICE_URL}/chat",
                json={"message": message},
                headers={
                    "X-User-Id": __user__["id"],
                    "X-Session-Id": __metadata__["chat_id"],
                },
            ) as response:
                response.raise_for_status()

                async for event, payload in sse_frames(response):
                    if event == "token":
                        yield payload["text"]
                    elif event == "tool_start":
                        # done=False is what spins the indicator.
                        await status(describe_call(payload["name"], payload.get("input")), False)
                    elif event == "tool_end":
                        ok = payload.get("status") == "success"
                        verb = "done in" if ok else "failed after"
                        # done=True settles this line; a later tool_start starts
                        # a new one, so the last line stays on screen.
                        await status(f"{payload['name']} {verb} {payload['seconds']}s", True)
                    elif event == "done":
                        return
