"""Behavior of the web_fetch tool.

All requests go through httpx.MockTransport, so nothing here touches the network.
"""

import asyncio

import httpx
import pytest

from agent.tools import web_fetch as wf


def serve(monkeypatch, body, content_type="text/html; charset=utf-8", status=200, url=None):
    """Point web_fetch at a canned response instead of the network."""

    def handler(request):
        return httpx.Response(
            status,
            content=body,
            headers={"content-type": content_type},
            request=request,
        )

    real_client = httpx.AsyncClient

    def fake_client(**kwargs):
        return real_client(transport=httpx.MockTransport(handler), **kwargs)

    monkeypatch.setattr(wf.httpx, "AsyncClient", fake_client)


def fetch(url="https://example.com/"):
    return asyncio.run(wf.web_fetch(url))


PAGE = """
<html>
  <head>
    <title>  Example   Domain </title>
    <style>body { color: red }</style>
    <script>var tracking = "should not appear";</script>
  </head>
  <body>
    <nav>Home</nav>
    <h1>Heading</h1>
    <p>First&nbsp;paragraph.</p>
    <p>Second paragraph.</p>
    <noscript>Enable JavaScript</noscript>
  </body>
</html>
"""


def test_html_reduced_to_title_and_visible_text(monkeypatch):
    serve(monkeypatch, PAGE)

    result = fetch()

    assert result.startswith("# Example Domain\nhttps://example.com/")
    assert "First paragraph." in result
    assert "Second paragraph." in result
    # Script, style and noscript bodies are markup, not content.
    assert "should not appear" not in result
    assert "color: red" not in result
    assert "Enable JavaScript" not in result


def test_block_tags_keep_words_apart(monkeypatch):
    serve(monkeypatch, "<html><body><p>one</p><p>two</p></body></html>")

    assert "onetwo" not in fetch()


def test_long_page_is_truncated(monkeypatch):
    serve(monkeypatch, "<html><body><p>" + ("word " * 20_000) + "</p></body></html>")

    result = fetch()

    assert "[truncated at 20000 characters]" in result
    # Header and truncation marker are the only things past the cap.
    assert len(result) < wf.MAX_TEXT_CHARS + 200


def test_oversized_response_stops_downloading(monkeypatch):
    serve(monkeypatch, b"<html><body><p>" + (b"x" * 5_000_000) + b"</p></body></html>")

    result = fetch()

    assert "[truncated at 20000 characters]" in result


def test_non_text_content_is_described_not_returned(monkeypatch):
    serve(monkeypatch, b"\x89PNG\r\n\x1a\n" + b"\x00" * 100, content_type="image/png")

    result = fetch()

    assert "image/png" in result
    assert "Not text" in result


def test_json_passes_through_without_html_stripping(monkeypatch):
    serve(monkeypatch, '{"answer": 42}', content_type="application/json")

    result = fetch()

    assert '{"answer": 42}' in result
    # No title line: JSON has no <title> to find.
    assert not result.startswith("#")


def test_http_error_propagates(monkeypatch):
    """Strands turns the exception into an error ToolResult, which the UI renders."""
    serve(monkeypatch, "nope", status=404)

    with pytest.raises(httpx.HTTPStatusError):
        fetch()


def test_page_with_no_text_says_so(monkeypatch):
    serve(monkeypatch, "<html><body><script>x=1</script></body></html>")

    assert "[no readable text]" in fetch()
