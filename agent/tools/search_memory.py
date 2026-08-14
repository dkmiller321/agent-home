"""On-demand memory queries, exposed to the agent as a tool."""

from strands import tool
from strands.tools.decorator import DecoratedFunctionTool

from agent.memory import query_memory


def build_search_memory(peer_id: str) -> DecoratedFunctionTool:
    """Bind the memory tool to one user's peer ID.

    Unlike current_time and web_fetch this cannot be a module-level tool: the
    peer ID arrives with the request, and the model must not be able to pass
    someone else's. Closing over it keeps it out of the tool's schema.
    """

    @tool
    async def search_memory(question: str) -> str:
        """Ask what is known about this user from previous conversations.

        A summary is already in your system prompt. Use this when you need
        something more specific than that summary covers — a detail mentioned
        once, a preference, something from a conversation weeks ago.

        Args:
            question: A natural-language question about the user, such as
                "what editor do they use?" or "what are they working on?"
        """
        return await query_memory(peer_id, question)

    return search_memory
