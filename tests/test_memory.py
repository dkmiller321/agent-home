"""Behavior of the context block that gets injected into the system prompt.

`format_context` is the only part of memory.py with logic rather than calls, and
it is where a wrong answer is silent: an empty block means the model quietly
behaves as though it has never met the user.
"""

from honcho.api_types import PeerContextResponse

from agent.memory import format_context


def context(card=None, representation=None):
    return PeerContextResponse(
        peer_id="kyle", target_id="kyle", peer_card=card, representation=representation
    )


def test_card_facts_become_a_list():
    formatted = format_context(context(card=["Uses Neovim.", "Lives in Denver."]))

    assert formatted == "- Uses Neovim.\n- Lives in Denver."


def test_card_and_representation_are_kept_apart():
    """One is short facts, the other is prose. Running them together reads as noise."""
    formatted = format_context(
        context(card=["Uses Neovim."], representation="Kyle is building a home agent.")
    )

    assert formatted == "- Uses Neovim.\n\nKyle is building a home agent."


def test_representation_alone_needs_no_bullets():
    assert format_context(context(representation="Kyle is a runner.")) == "Kyle is a runner."


def test_new_user_produces_nothing_rather_than_an_empty_heading():
    """A first-ever turn, or one still sitting in the deriver's queue."""
    assert format_context(context()) == ""


def test_whitespace_only_representation_counts_as_nothing():
    assert format_context(context(representation="   \n  ")) == ""
