"""Current time tool."""

from datetime import datetime

from strands import tool


@tool
def current_time() -> str:
    """Get the current local date and time, in ISO-8601 format with UTC offset."""
    return datetime.now().astimezone().isoformat()
