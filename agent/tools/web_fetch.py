"""Web fetch tool."""

import re
from html.parser import HTMLParser

import httpx
from strands import tool

TIMEOUT_SECONDS = 15.0
# Capped while streaming, so an enormous page is never fully downloaded.
MAX_RESPONSE_BYTES = 2_000_000
# Roughly 5k tokens. A long page must not crowd out the conversation.
MAX_TEXT_CHARS = 20_000

# httpx's default User-Agent is rejected outright by a lot of sites.
USER_AGENT = "Mozilla/5.0 (compatible; agent-home/0.1)"

# Elements whose text is markup, not content. `head` is not skipped: its only
# textual children are `title` (wanted) and `script`/`style` (already here).
SKIP_TAGS = frozenset({"script", "style", "noscript", "svg", "template"})

# Elements that imply a line break, so words either side do not run together.
BLOCK_TAGS = frozenset(
    {
        "p", "div", "br", "hr", "li", "tr", "section", "article", "header",
        "footer", "nav", "aside", "blockquote", "pre", "table",
        "h1", "h2", "h3", "h4", "h5", "h6",
    }
)

TEXTUAL_CONTENT_TYPES = ("text/", "json", "xml", "html", "javascript")

# convert_charrefs turns &nbsp; into U+00A0, which str.strip() does not consider
# whitespace. Named rather than written literally so it stays visible in a diff.
NBSP = " "


class _TextExtractor(HTMLParser):
    """Collect visible text and the document title from an HTML stream."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._parts: list[str] = []
        self._skip_depth = 0
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in SKIP_TAGS:
            self._skip_depth += 1
        elif tag == "title":
            self._in_title = True
        elif tag in BLOCK_TAGS:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP_TAGS:
            # Clamped: malformed pages close tags they never opened.
            self._skip_depth = max(0, self._skip_depth - 1)
        elif tag == "title":
            self._in_title = False
        elif tag in BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        if self._in_title:
            self.title += data
        else:
            self._parts.append(data)

    def text(self) -> str:
        return collapse_whitespace("".join(self._parts))


def collapse_whitespace(text: str) -> str:
    """Squeeze layout whitespace so the result reads as prose, not as a page."""
    lines = [re.sub(f"[ \t\r{NBSP}]+", " ", line).strip() for line in text.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def html_to_text(html: str) -> tuple[str, str]:
    """Reduce an HTML document to (title, visible text)."""
    extractor = _TextExtractor()
    extractor.feed(html)
    extractor.close()
    return collapse_whitespace(extractor.title), extractor.text()


@tool
async def web_fetch(url: str) -> str:
    """Fetch a URL and return its readable text content.

    Use this to read web pages, documentation, articles, or JSON APIs — anything
    the answer depends on that is not already known. HTML is reduced to plain
    text, and long pages are truncated.

    Args:
        url: Absolute http:// or https:// URL to fetch.
    """
    async with httpx.AsyncClient(
        follow_redirects=True,
        timeout=TIMEOUT_SECONDS,
        headers={"User-Agent": USER_AGENT},
    ) as client:
        async with client.stream("GET", url) as response:
            response.raise_for_status()
            content_type = response.headers.get("content-type", "")

            chunks: list[bytes] = []
            size = 0
            async for chunk in response.aiter_bytes():
                chunks.append(chunk)
                size += len(chunk)
                if size >= MAX_RESPONSE_BYTES:
                    break

            final_url = str(response.url)
            encoding = response.charset_encoding or "utf-8"

    raw = b"".join(chunks)[:MAX_RESPONSE_BYTES]

    if not any(kind in content_type for kind in TEXTUAL_CONTENT_TYPES):
        return (
            f"{final_url} returned {content_type or 'an unknown type'} "
            f"({size} bytes). Not text; nothing to read."
        )

    body = raw.decode(encoding, errors="replace")

    if "html" in content_type:
        title, text = html_to_text(body)
    else:
        title, text = "", collapse_whitespace(body)

    if len(text) > MAX_TEXT_CHARS:
        text = f"{text[:MAX_TEXT_CHARS]}\n\n[truncated at {MAX_TEXT_CHARS} characters]"

    header = f"# {title}\n{final_url}" if title else final_url
    return f"{header}\n\n{text}" if text else f"{header}\n\n[no readable text]"
