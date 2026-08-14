"""Strands agent definition."""

from strands import Agent
from strands.models.openai import OpenAIModel

from agent.settings import settings
from agent.tools.current_time import current_time
from agent.tools.search_memory import build_search_memory
from agent.tools.web_fetch import web_fetch

SYSTEM_PROMPT = (
    "You are a helpful assistant. When a tool can answer part of the question, "
    "call it rather than guessing."
)

# Appended only when there is something to say. Framing matters more than it
# looks: without it the model treats recalled facts as part of the user's latest
# message and opens by reciting them back.
MEMORY_PREAMBLE = """

What you already know about this user, from earlier conversations:

{context}

That is background you carry in, not something the user has just told you. Use
it where it is relevant and otherwise leave it alone — do not recite it, and do
not announce that you remembered. Call search_memory when you need something
more specific than the above."""


def build_agent(peer_id: str, memory_context: str) -> Agent:
    """Build an agent for a single request.

    One instance per request, not a shared module-level one: an Agent carries its
    conversation history on the instance and defaults to
    ConcurrentInvocationMode.THROW, so sharing it would leak history between
    unrelated callers and raise on overlapping requests. Construction is local
    setup only — no network call.

    `memory_context` is already-fetched text rather than something looked up
    here, so this stays synchronous and the caller decides when to pay for the
    round trip. `peer_id` is only used to bind the memory tool.
    """
    system_prompt = SYSTEM_PROMPT
    if memory_context:
        system_prompt += MEMORY_PREAMBLE.format(context=memory_context)

    model = OpenAIModel(
        client_args={
            "api_key": settings.openrouter_api_key,
            "base_url": settings.openrouter_base_url,
        },
        model_id=settings.agent_model,
    )
    return Agent(
        model=model,
        tools=[current_time, web_fetch, build_search_memory(peer_id)],
        system_prompt=system_prompt,
        callback_handler=None,
    )
