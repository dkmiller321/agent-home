# The agent service. Runs `python -m agent.main`, so host/port/log level come
# from the same settings object the host-run path uses — there is no second
# place where the service is configured.

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Dependencies before source: this layer is rebuilt only when the lock changes.
# pyproject declares no build-system, so uv treats the project as non-packaged
# and installs only its dependencies.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY agent/ agent/

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

CMD ["python", "-m", "agent.main"]
