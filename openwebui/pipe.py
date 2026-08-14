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
# Everything it does: forward the latest user message to /chat, and turn the SSE
# frames that come back into the string chunks Open WebUI streams to the browser.
# Agent behavior belongs on the other side of that HTTP call.

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

    async def pipe(self, body: dict, __user__: dict) -> AsyncIterator[str]:
        """Stream one turn.

        Open WebUI's user ID is passed through as a header. The agent only logs
        it today; it becomes the Honcho peer ID in stage 4.
        """
        message = body["messages"][-1]["content"]

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.valves.AGENT_SERVICE_URL}/chat",
                json={"message": message},
                headers={"X-User-Id": __user__["id"]},
            ) as response:
                response.raise_for_status()

                async for event, payload in sse_frames(response):
                    # `tool` frames are read and dropped: rendering them as status
                    # events is stage 3.
                    if event == "token":
                        yield payload["text"]
                    elif event == "done":
                        return
