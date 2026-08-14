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


def use_agent(monkeypatch, events, context=""):
    """Run stream_chat against fixed events and a stubbed Honcho.

    Returns `(built, written)`: the arguments `build_agent` was called with, and
    the turns `record_turn` was asked to persist. Between them they cover both
    halves of the memory path without a Honcho to talk to.
    """
    built = []
    written = []

    def build_agent(peer_id, memory_context):
        built.append((peer_id, memory_context))
        return FakeAgent(events)

    async def load_context(peer_id):
        return context

    async def record_turn(peer_id, session_id, user_message, assistant_message):
        written.append((peer_id, session_id, user_message, assistant_message))

    monkeypatch.setattr(main, "build_agent", build_agent)
    monkeypatch.setattr(main, "load_context", load_context)
    monkeypatch.setattr(main, "record_turn", record_turn)
    return built, written


def drain(message, peer_id="u1", session_id="s1"):
    async def collect():
        return [frame async for frame in main.stream_chat(message, peer_id, session_id)]

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
    use_agent(
        monkeypatch,
        [
            # Input deltas carry a half-built JSON string and are ignored;
            # the assistant message below is what gets announced.
            {"type": "tool_use_stream", "current_tool_use": {"toolUseId": "t1", "input": '{"ur'}},
            assistant_tool_use("t1", "web_fetch", {"url": "https://example.com"}),
            tool_results({"toolUseId": "t1", "status": "success"}),
            {"data": "The page "},
            {"data": "says hello."},
        ],
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
    use_agent(
        monkeypatch,
        [
            assistant_tool_use("t1", "web_fetch", {"url": "https://nope.invalid"}),
            tool_results({"toolUseId": "t1", "status": "error"}),
        ],
    )

    _, payload = parse(drain("fetch it"))[1]

    assert payload["status"] == "error"
    assert payload["name"] == "web_fetch"


def test_concurrent_tools_each_get_their_own_frames(monkeypatch):
    """Results for one cycle arrive batched in a single message."""
    use_agent(
        monkeypatch,
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
        ],
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
    use_agent(
        monkeypatch,
        [
            {"data": "Hello."},
            {"message": {"role": "assistant", "content": [{"text": "Hello."}]}},
        ],
    )

    assert parse(drain("hi")) == [("token", {"text": "Hello."}), ("done", {})]


def test_token_text_with_newlines_stays_one_frame(monkeypatch):
    use_agent(monkeypatch, [{"data": "line one\n\nline two"}])

    frames = drain("hi")

    assert parse(frames)[0] == ("token", {"text": "line one\n\nline two"})
    assert len(frames) == 2


def test_loaded_context_is_handed_to_the_agent(monkeypatch):
    """The automatic half of memory: nothing the model does decides this."""
    built, _ = use_agent(monkeypatch, [{"data": "Hi."}], context="- Kyle uses Neovim.")

    drain("hi", peer_id="kyle")

    assert built == [("kyle", "- Kyle uses Neovim.")]


def test_completed_turn_is_written_as_both_messages(monkeypatch):
    """What gets stored is the user's text and the assembled reply, not frames."""
    _, written = use_agent(monkeypatch, [{"data": "one "}, {"data": "two"}])

    drain("what did I say?", peer_id="kyle", session_id="chat-9")

    assert written == [("kyle", "chat-9", "what did I say?", "one two")]


def test_nothing_is_written_while_tokens_are_still_arriving(monkeypatch):
    """The reply does not exist until the stream ends, so neither can the write."""
    _, written = use_agent(monkeypatch, [{"data": "one "}, {"data": "two"}])

    async def consume():
        async for frame in main.stream_chat("hi", "kyle", "chat-9"):
            if "token" in frame:
                assert written == []

    asyncio.run(consume())

    assert len(written) == 1


def test_tool_output_is_not_part_of_the_recorded_reply(monkeypatch):
    """Only assistant text is stored; tool traffic is UI detail, not memory."""
    _, written = use_agent(
        monkeypatch,
        [
            assistant_tool_use("t1", "current_time", {}),
            tool_results({"toolUseId": "t1", "status": "success"}),
            {"data": "It is noon."},
        ],
    )

    drain("what time is it?")

    assert written[0][3] == "It is noon."
