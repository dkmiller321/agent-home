# agent-home

A locally-hosted chat application backed by an agent that uses tools and
remembers you across sessions.

Tell it something on Monday, start a fresh chat on Friday, and it still knows.
That is the whole point of the project; everything below exists to make that
work.

This is a home project. Decisions favour "understandable on a laptop" over
"scales to a thousand users." `DESIGN.md` is the source of truth for why things
are the way they are; `CLAUDE.md` holds the working conventions.

## What it is

Three off-the-shelf open-source pieces, plus a thin layer of our own code:

| Piece | Role |
|---|---|
| [Open WebUI](https://github.com/open-webui/open-webui) | Chat interface — accounts, history, streaming, mobile |
| [Strands Agents](https://github.com/strands-agents/sdk-python) | The agent — model, system prompt, tools, agent loop |
| [Honcho](https://github.com/plastic-labs/honcho) | Memory — extracts facts from conversations into a per-user profile |

Ours is the glue: a FastAPI service wrapping the Strands agent, and an Open WebUI
Pipe function connecting the UI to it.

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
                   (inference)      (memory)     (current_time,
                                        |          web_fetch,
                                  ┌─────┴─────┐   search_memory)
                                  v           v
                              Postgres      Redis
                             (pgvector)   (deriver queue)
```

The agent lives behind HTTP rather than inside Open WebUI. The Pipe is a thin
client, so the agent stays testable with `curl` and the frontend could be
swapped without touching agent code.

### A turn, start to finish

1. You send a message in Open WebUI.
2. The Pipe forwards it to the agent service with your user ID and chat ID as
   headers.
3. The agent fetches your profile from Honcho and injects it into the system
   prompt.
4. Strands runs its loop against OpenRouter, calling tools as needed.
5. Tool calls stream back as `status` events, so you can watch it work.
6. The reply streams back. Both messages are written to Honcho, whose deriver
   extracts facts from them in the background.

### Memory is hybrid, deliberately

Two paths, both intentional:

- **Injected** — your profile goes into the system prompt every turn, so the
  model cannot forget to check.
- **Queried** — a `search_memory` tool for anything more specific than the
  summary covers.

Reads are scoped to a **peer**, never to a session. That is what makes recall
survive starting a new chat: Honcho's peer context has no session parameter, so
it answers from everything the workspace knows about you. Open WebUI's user ID
*is* the Honcho peer ID, and its chat ID *is* the session ID — no identifiers of
our own.

## Running it

**Prerequisites:** Docker with Compose, and an OpenRouter API key. For host-side
development, Python 3.11+ and [uv](https://github.com/astral-sh/uv).

```bash
cp .env.example .env
```

Edit `.env` and set, at minimum:

| Variable | Notes |
|---|---|
| `OPENROUTER_API_KEY` | One key serves everything |
| `LLM_OPENAI_API_KEY` | Honcho's copy of the same key |
| `POSTGRES_PASSWORD` | Must match the password inside `DB_CONNECTION_URI` |
| `WEBUI_SECRET_KEY` | Any random string |

**Set a spend limit on the OpenRouter key.** Honcho calls a model on every
message and can outspend the agent.

Then:

```bash
docker compose up -d --build
```

Six services come up in dependency order: `postgres` and `redis` first, then
`honcho` (which runs its migrations on start), then `honcho-deriver`, `agent`
and `open-webui`.

| Service | URL |
|---|---|
| Open WebUI | http://localhost:3000 |
| Agent service | http://localhost:8080 |
| Honcho API | http://localhost:8000 (`/docs` for the API browser) |

Postgres and Redis are deliberately not published — reach them through
`docker compose exec`.

### Installing the Pipe

Open WebUI loads the Pipe from its own database, not from this repo, so it has
to be pasted in:

1. http://localhost:3000 → create an account (the first one is admin)
2. Admin Settings → Functions → **+**
3. Paste the contents of `openwebui/pipe.py`, save, enable it
4. Pick **Agent Home** from the model dropdown

**Re-paste it whenever `openwebui/pipe.py` changes.** The installed copy is a
snapshot; nothing syncs it. Open WebUI reformats the code on save, which is
cosmetic only.

## Verifying it works

The agent is reachable independently of the UI, which is the fastest way to test
memory. Use a peer ID you have not used before — an existing one already knows
things.

```bash
# Say something
curl -sN -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -H "X-User-Id: alex" -H "X-Session-Id: session-one" \
  -d '{"message":"I ride a 1998 Bridgestone RB-1 in Prussian blue."}'

# Wait for the deriver, then ask from a *different* session
curl -sN -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -H "X-User-Id: alex" -H "X-Session-Id: session-two" \
  -d '{"message":"What bike do I ride?"}'
```

Raw SSE is unreadable; pipe it through this for just the reply:

```bash
... | python -c "import sys,json; print(''.join(
    json.loads(l[6:]).get('text','') for l in sys.stdin if l.startswith('data: ')))"
```

**Memory is eventually consistent.** Say something and immediately ask about it
and it will not be there. To know whether the deriver has caught up:

```bash
docker compose exec -T postgres psql -U honcho -d honcho \
  -c "select task_type, processed from queue order by id desc limit 5;"
```

`processed = f` means still queued. Expect roughly 60–120 seconds.

The agent's own log tells you whether memory is flowing:

```
chat request from user alex in session session-two
loaded 272 chars of context for peer alex     <- 0 on a first-ever turn
recorded turn for peer alex in session session-two
```

## Inspecting memory

`documents` is where memory actually lives — the derived facts, embedded.
Everything else is bookkeeping.

```bash
docker compose exec -it postgres psql -U honcho -d honcho
```

```sql
select observer, observed, content from documents order by created_at;
select peer_name, session_name, left(content, 60) from messages order by created_at;
```

`observer = observed` is the global self-representation, the one injected into
the system prompt.

Query on `name` / `peer_name` / `session_name`, **not** `id` — `sessions.id` is
a nanoid Honcho generates, while `name` holds the ID you passed.

Without SQL:

```bash
curl -s http://localhost:8000/v3/workspaces/agent-home/peers/alex/context | python -m json.tool
```

## Development

The agent can run on the host against the containerised services:

```bash
uv sync
uv run python -m agent.main
```

Point the Pipe's `AGENT_SERVICE_URL` valve at `http://host.docker.internal:8080`,
and set `HONCHO_BASE_URL=http://localhost:8000` in `.env`.

```bash
uv run pytest
```

Tests cover the SSE translation and both halves of the memory path with Honcho
stubbed out; they need no running services.

### Layout

```
agent/
  main.py              FastAPI app, SSE streaming, memory bracketing the turn
  agent.py             Strands agent, system prompt, memory injection
  memory.py            Honcho read/write
  settings.py          Pydantic settings, read once at startup
  tools/               current_time, web_fetch, search_memory
openwebui/pipe.py      Pipe function — pasted into Open WebUI, not imported
tests/                 pytest, mirroring agent/
docker-compose.yml
```

## Things worth knowing

**The embedding dimension is permanent.** pgvector bakes it into the schema on
first run. It is `openai/text-embedding-3-small` at 1536; changing it later
means a migration and a full re-embed. Decide before the first `docker compose
up`. To confirm what actually got created:

```bash
docker compose exec -T postgres psql -U honcho -d honcho -c "\d documents" | grep embedding
#  embedding | vector(1536) | ...
```

**The deriver batches its work.** Honcho's default holds a batch for 30 minutes
or until it reaches ~512 tokens, so a single short message takes half an hour to
become memory. `.env.example` sets
`DERIVER_REPRESENTATION_BATCH_MAX_AGE_SECONDS=60` instead, trading a few extra
extraction calls for recall inside a minute.

**Open WebUI talks to itself through your model.** Title, tag and follow-up
generation are routed through whichever model is selected — ours. Left alone,
one browser message arrives as four requests, and Honcho files the UI's prompt
engineering as facts about you. The Pipe forwards Open WebUI's `__task__` as an
`X-Task` header and the agent answers those without remembering them. You can
also point task generation at a cheaper model in Admin → Settings → Interface,
which the fix does not do for you.

**Prefer plugins to forks.** Open WebUI ships releases constantly. Anything
built on its extension points survives upgrades; anything patched into its
source is a rebase every time.

## Resetting

```bash
docker compose down          # stop, keep data
docker compose down -v       # stop and destroy memory, including the schema
```

`down -v` is also the only moment the embedding model can change without a
migration.

## Not doing

Auth beyond Open WebUI's built-in accounts. Public exposure. Multi-user scale.
HA Postgres. Later problems, and probably never.
