# Agent Project — Design Overview

> Working name: `agent-home`. Rename as you like.

## Purpose

A locally-hosted chat application backed by a real agent — one that uses tools,
and that actually remembers you across sessions.

This is a home project. The goals are learning and daily personal use, not
production deployment. Design decisions favor "understandable on a laptop" over
"scales to a thousand users."

## What It Is

Three off-the-shelf open-source pieces plus a thin layer of our own code:

- **Open WebUI** — the chat interface. Handles accounts, history, streaming, mobile.
- **Strands Agents** — the agent itself. Model, system prompt, tools, agent loop.
- **Honcho** — the memory service. Extracts facts from conversations and builds
  a persistent profile per user.

Our code is the glue: a FastAPI service that wraps the Strands agent, and an
Open WebUI Pipe function that connects the UI to it.

## Architecture

```
Browser
   |
   v
Open WebUI  ──(Pipe function)──>  Agent Service (FastAPI + Strands)
                                        |
                        ┌───────────────┼───────────────┐
                        v               v               v
                   OpenRouter        Honcho          Tools
                   (inference)      (memory)        (MCP, custom)
                                        |
                                  ┌─────┴─────┐
                                  v           v
                              Postgres      Redis
                             (pgvector)   (workers)
```

### Request flow

1. User sends a message in Open WebUI.
2. The Pipe function forwards it to the Agent Service, passing the Open WebUI
   user ID along.
3. Agent Service fetches that user's context from Honcho and injects it into
   the system prompt.
4. Strands runs its agent loop against OpenRouter, calling tools as needed.
5. Tool calls are emitted back to the UI as `status` events so the user can
   watch the agent work.
6. The response streams back. Both messages are written to Honcho, which
   processes them in the background.

## Design Decisions

**Agent lives behind HTTP, not inside Open WebUI.** The Pipe function is a thin
client. This keeps the agent testable with `curl` and means we could swap the
frontend later without touching agent code.

**Memory is hybrid, not tool-only.** Context is injected into the system prompt
automatically each turn, so the model can't "forget" to check. A separate tool
is exposed for deeper on-demand queries. Automatic for the common case,
deliberate for the unusual one.

**Open WebUI user ID maps to Honcho peer ID.** Without this, every user shares
one memory blob.

**One LLM provider.** OpenRouter serves both chat and embeddings through a
single key and base URL, for the agent and for Honcho.

**Embedding model is `openai/text-embedding-3-small` at 1536 dimensions.**
Decided, not a default to be casually revised. Cheap, widely supported, and
1536 is the dimension most tooling assumes — including Honcho's own
`EMBEDDING_VECTOR_DIMENSIONS` default. pgvector fixes this in the schema at
first run, so changing it later costs a migration and a full re-embed. Treat it
as settled unless there is a specific reason to pay that.

## Dependencies

### Services (Docker Compose)

| Service | Role |
|---|---|
| `open-webui` | Chat frontend |
| `agent` | Our FastAPI + Strands service |
| `honcho` | Memory API |
| `honcho-deriver` | Background worker for fact extraction |
| `postgres` | Honcho storage (needs pgvector) |
| `redis` | Worker coordination |

Open WebUI keeps its own state in a Docker volume — it does not share the
Postgres instance.

### External

- **OpenRouter** — one API key. Chat model for the agent, a cheaper model for
  Honcho's extraction, an embedding model for vector storage.

### Python

- `strands-agents[openai]` — agent framework, OpenAI-compatible provider for OpenRouter
- `honcho-ai` — memory client
- `fastapi` + `uvicorn[standard]` — the agent service. The `standard` extra brings
  `httptools` and `websockets`, which matter for streaming; `uvloop` is skipped
  automatically on Windows.
- `pydantic-settings` — the startup settings object. Pydantic v2 moved
  `BaseSettings` out of `pydantic` into this package.
- `pytest` (dev group) — tests

## Repo Layout

```
agent-home/
├── docker-compose.yml
├── pyproject.toml
├── .env.example
├── .gitignore
├── agent/
│   ├── main.py           # FastAPI app, SSE streaming
│   ├── agent.py          # Strands agent definition
│   ├── memory.py         # Honcho read/write
│   └── tools/            # Custom Strands tools
├── openwebui/
│   └── pipe.py           # Pipe function, installed via Open WebUI admin UI
├── tests/                # pytest, mirroring the agent/ layout
└── DESIGN.md
```

## Build Order

Bring services up one at a time. Debugging six unfamiliar containers
simultaneously is how home projects die.

1. Strands agent + FastAPI. Verify with `curl`. No memory, no UI.
2. Add Open WebUI and the Pipe function. Verify chat and streaming.
3. Add tools and `status` event rendering.
4. Add Honcho last, once a broken response is obviously its fault.

## Things To Know

**Memory is eventually consistent.** Honcho's deriver runs in the background.
Say something and immediately ask about it, and it may not be there yet. This is
expected, not a bug.

**Honcho can outspend the agent.** It calls a model on every message. Point it
at something cheap and set a spend limit on the OpenRouter key.

**Embedding dimension is permanent-ish.** pgvector bakes it into the schema.
Pick the embedding model before the first run; changing it later means a
migration and a full re-embed.

**Prefer plugins to forks.** Open WebUI ships releases constantly. Anything
built on its extension points survives upgrades; anything patched into its
source becomes a rebase every time.

## Not Doing

Auth beyond Open WebUI's built-in accounts. Public exposure. Multi-user scale.
HA Postgres. Any of this is a later problem, and probably never.
