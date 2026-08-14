"""Behavior of the Strands-event -> SSE translation."""

import asyncio
import json

from agent import main


class FakeAgent:
    def __init__(self, events):
        self._events = events

    async def stream_async(self, message):
        for event in self._events:
            yield event


def drain(message):
    async def collect():
        return [frame async for frame in main.stream_chat(message)]

    return asyncio.run(collect())


def parse(frames):
    parsed = []
    for frame in frames:
        event_line, data_line = frame.strip().split("\n")
        parsed.append((event_line.removeprefix("event: "), json.loads(data_line.removeprefix("data: "))))
    return parsed


def test_tool_announced_once_then_tokens_stream(monkeypatch):
    tool_use = {"toolUseId": "abc123", "name": "current_time", "input": ""}
    monkeypatch.setattr(
        main,
        "build_agent",
        lambda: FakeAgent(
            [
                {"type": "tool_use_stream", "current_tool_use": tool_use},
                {"type": "tool_use_stream", "current_tool_use": {**tool_use, "input": "{}"}},
                {"type": "tool_result", "tool_result": {"status": "success"}},
                {"data": "It is "},
                {"data": "3pm."},
            ]
        ),
    )

    assert parse(drain("what time is it?")) == [
        ("tool", {"name": "current_time"}),
        ("token", {"text": "It is "}),
        ("token", {"text": "3pm."}),
        ("done", {}),
    ]


def test_token_text_with_newlines_stays_one_frame(monkeypatch):
    monkeypatch.setattr(main, "build_agent", lambda: FakeAgent([{"data": "line one\n\nline two"}]))

    frames = drain("hi")

    assert parse(frames)[0] == ("token", {"text": "line one\n\nline two"})
    assert len(frames) == 2
