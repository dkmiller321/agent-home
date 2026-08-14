"""Honcho memory: the read before a turn and the write after it.

Both directions are deliberate. `load_context` runs every turn and its result
lands in the system prompt, so the model cannot forget to check; `query_memory`
backs the tool, for the times a summary is not specific enough.

Every read here is scoped to a peer and never to a session. That is what makes
recall survive starting a new chat: `peer.context()` takes no session argument,
so it answers from everything the workspace knows about that peer. Sessions
exist only so writes land somewhere and the deriver has a conversation to
reason over.
"""

import logging

from honcho import Honcho
from honcho.api_types import PeerContextResponse, SessionPeerConfig

from agent.settings import settings

logger = logging.getLogger(__name__)

# Constructing this opens an httpx client and makes no network call, so module
# level is fine — including on Windows, where no event loop exists yet at import
# time. The async client behind `.aio` is built lazily on first use.
honcho = Honcho(
    api_key=settings.honcho_api_key,
    base_url=settings.honcho_base_url,
    workspace_id=settings.honcho_workspace_id,
)

# Left to itself Honcho would derive a representation of our own assistant too,
# at the price of a model call per message. Only the user's side is worth that.
ASSISTANT_CONFIG = SessionPeerConfig(observe_me=False, observe_others=False)


def format_context(context: PeerContextResponse) -> str:
    """Render a peer's context as the block that goes into the system prompt.

    The card is a list of short facts and the representation is prose, so they
    are joined rather than merged. Returns an empty string when Honcho has
    nothing yet — a first-time user, or one whose opening message is still in
    the deriver's queue. Callers use that emptiness to skip injection entirely.
    """
    sections = []
    if context.peer_card:
        sections.append("\n".join(f"- {fact}" for fact in context.peer_card))
    if context.representation and context.representation.strip():
        sections.append(context.representation.strip())
    return "\n\n".join(sections)


async def load_context(peer_id: str) -> str:
    """Fetch everything known about a user, across all their past sessions."""
    peer = await honcho.aio.peer(peer_id)
    context = await peer.aio.context()
    formatted = format_context(context)
    logger.info("loaded %s chars of context for peer %s", len(formatted), peer_id)
    return formatted


async def record_turn(
    peer_id: str,
    session_id: str,
    user_message: str,
    assistant_message: str,
) -> None:
    """Write both halves of a completed turn.

    `peer` and `session` are get-or-create, so this is also what brings a new
    user and a new chat into existence. Returning does not mean the turn has
    been understood: the deriver reads it from a queue afterwards, which is why
    memory is eventually consistent.
    """
    user = await honcho.aio.peer(peer_id)
    assistant = await honcho.aio.peer(settings.honcho_assistant_peer_id)
    session = await honcho.aio.session(
        session_id, peers=[user, (assistant, ASSISTANT_CONFIG)]
    )
    await session.aio.add_messages(
        [user.message(user_message), assistant.message(assistant_message)]
    )
    logger.info("recorded turn for peer %s in session %s", peer_id, session_id)


async def query_memory(peer_id: str, question: str) -> str:
    """Put a question about the user to Honcho's dialectic endpoint.

    `reasoning_level` is medium because that is the level configured in .env.
    Honcho needs a model config per level and only that one is set; asking for
    another would fail server-side rather than fall back.
    """
    answer = await (await honcho.aio.peer(peer_id)).aio.chat(
        question, reasoning_level="medium"
    )
    # None means the representation had nothing to say, not that a call failed.
    return answer or "Nothing is known about that yet."
