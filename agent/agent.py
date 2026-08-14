"""Strands agent definition."""

from strands import Agent
from strands.models.openai import OpenAIModel

from agent.settings import settings
from agent.tools.current_time import current_time
from agent.tools.web_fetch import web_fetch

SYSTEM_PROMPT = (
    "You are a helpful assistant. When a tool can answer part of the question, "
    "call it rather than guessing."
)


def build_agent() -> Agent:
    """Build an agent for a single request.

    One instance per request, not a shared module-level one: an Agent carries its
    conversation history on the instance and defaults to
    ConcurrentInvocationMode.THROW, so sharing it would leak history between
    unrelated callers and raise on overlapping requests. Construction is local
    setup only — no network call.
    """
    model = OpenAIModel(
        client_args={
            "api_key": settings.openrouter_api_key,
            "base_url": settings.openrouter_base_url,
        },
        model_id=settings.agent_model,
    )
    return Agent(
        model=model,
        tools=[current_time, web_fetch],
        system_prompt=SYSTEM_PROMPT,
        callback_handler=None,
    )
