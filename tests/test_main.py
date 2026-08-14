"""Behavior of the Strands-event -> SSE translation.

The event dicts below are the shapes `Agent.stream_async` actually yields.
Notably absent is `{"type": "tool_result"}`: `ToolResultEvent` sets
`is_callback_event` to False and `stream_async` yields callback events only, so
a test fed that shape would be testing a stream that cannot happen.
"""

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
        parsed.append(
            (event_line.removeprefix("event: "), json.loads(data_line.removeprefix("data: ")))
        )
    return parsed


def assistant_tool_use(tool_use_id, name, tool_input):
    return {
        "message": {
            "role": "assistant",
            "content": [
                {"toolUse": {"toolUseId": tool_use_id, "name": name, "input": tool_input}}
            ],
        }
    }


def tool_results(*results):
    return {
        "message": {
            "role": "user",
            "content": [{"toolResult": result} for result in results],
        }
    }


def test_tool_call_brackets_the_token_stream(monkeypatch):
    monkeypatch.setattr(
        main,
        "build_agent",
        lambda: FakeAgent(
            [
                # Input deltas carry a half-built JSON string and are ignored;
                # the assistant message below is what gets announced.
                {"type": "tool_use_stream", "current_tool_use": {"toolUseId": "t1", "input": '{"ur'}},
                assistant_tool_use("t1", "web_fetch", {"url": "https://example.com"}),
                tool_results({"toolUseId": "t1", "status": "success"}),
                {"data": "The page "},
                {"data": "says hello."},
            ]
        ),
    )

    events = parse(drain("what is on example.com?"))
    names = [name for name, _ in events]

    assert names == ["tool_start", "tool_end", "token", "token", "done"]

    start = events[0][1]
    assert start["name"] == "web_fetch"
    assert start["input"] == {"url": "https://example.com"}

    end = events[1][1]
    assert end["id"] == start["id"] == "t1"
    assert (end["name"], end["status"]) == ("web_fetch", "success")


def test_failed_tool_reports_error_status(monkeypatch):
    monkeypatch.setattr(
        main,
        "build_agent",
        lambda: FakeAgent(
            [
                assistant_tool_use("t1", "web_fetch", {"url": "https://nope.invalid"}),
                tool_results({"toolUseId": "t1", "status": "error"}),
            ]
        ),
    )

    _, payload = parse(drain("fetch it"))[1]

    assert payload["status"] == "error"
    assert payload["name"] == "web_fetch"


def test_concurrent_tools_each_get_their_own_frames(monkeypatch):
    """Results for one cycle arrive batched in a single message."""
    monkeypatch.setattr(
        main,
        "build_agent",
        lambda: FakeAgent(
            [
                {
                    "message": {
                        "role": "assistant",
                        "content": [
                            {"toolUse": {"toolUseId": "t1", "name": "current_time", "input": {}}},
                            {
                                "toolUse": {
                                    "toolUseId": "t2",
                                    "name": "web_fetch",
                                    "input": {"url": "https://example.com"},
                                }
                            },
                        ],
                    }
                },
                tool_results(
                    {"toolUseId": "t1", "status": "success"},
                    {"toolUseId": "t2", "status": "error"},
                ),
            ]
        ),
    )

    events = parse(drain("time and page please"))

    assert [name for name, _ in events] == [
        "tool_start",
        "tool_start",
        "tool_end",
        "tool_end",
        "done",
    ]
    assert [payload["id"] for _, payload in events[:4]] == ["t1", "t2", "t1", "t2"]
    assert [payload["name"] for _, payload in events[2:4]] == ["current_time", "web_fetch"]


def test_assistant_text_message_is_not_a_tool_frame(monkeypatch):
    """A plain answer produces tokens and nothing else."""
    monkeypatch.setattr(
        main,
        "build_agent",
        lambda: FakeAgent(
            [
                {"data": "Hello."},
                {"message": {"role": "assistant", "content": [{"text": "Hello."}]}},
            ]
        ),
    )

    assert parse(drain("hi")) == [("token", {"text": "Hello."}), ("done", {})]


def test_token_text_with_newlines_stays_one_frame(monkeypatch):
    monkeypatch.setattr(main, "build_agent", lambda: FakeAgent([{"data": "line one\n\nline two"}]))

    frames = drain("hi")

    assert parse(frames)[0] == ("token", {"text": "line one\n\nline two"})
    assert len(frames) == 2
