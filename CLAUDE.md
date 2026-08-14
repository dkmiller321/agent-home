# CLAUDE.md — Project Conventions

Read `DESIGN.md` first. It is the source of truth for architecture. If something
in this file contradicts it, ask rather than guessing.

## Stack

- Python 3.11+, FastAPI, `uv` for dependency management
- Strands Agents SDK (`strands-agents[openai]`) — agent framework
- Honcho (`honcho-ai`) — memory service
- Open WebUI — chat frontend, extended via a Pipe function
- OpenRouter — single provider for chat and embeddings
- Docker Compose for all services

## Conventions

- **Naming:** `snake_case` for functions and modules, `PascalCase` for classes.
- **Config:** everything through environment variables, read once at startup
  into a Pydantic settings object. No `os.getenv` scattered through the code.
- **Errors:** let exceptions propagate. FastAPI exception handlers at the edge.
  No blanket `try/except` around every call.
- **Async:** the agent path is async end to end. Do not mix in sync HTTP clients.
- **Logging:** stdlib `logging`, module-level logger, no custom wrapper.
- **Tests:** pytest, in `tests/`, mirroring the module layout. Test behavior,
  not structure.

## Hard Constraints

- **Do not add a dependency without asking first.** This includes transitive
  convenience libraries. The stack above is the stack.
- **Do not fork or patch Open WebUI's source.** All UI work goes through the
  Pipe function and its event system.
- **Do not invent abstraction layers.** No provider interfaces, no repository
  pattern, no plugin registries. One implementation means one concrete class.
- **Do not write defensive boilerplate.** No retry decorators, no circuit
  breakers, no logging middleware unless a real failure has motivated it.
- **Do not leave TODO comments or stub functions.** Either implement it or tell
  me it's out of scope.
- **Do not refactor outside the current stage's scope.** Note observations at
  the end instead.

## Working Agreement

- Propose a plan before writing code. Wait for confirmation.
- One stage per session. Stages are defined in `DESIGN.md` under Build Order.
- If a change would touch more than five files, stop and confirm scope.
- Nothing is "done" until it has actually run. State the command you ran and
  what you observed. Do not report success on unexecuted code.
- Surface risks and unrelated issues at the end as observations, not blockers.

## Architecture Notes

- The agent service is reachable over HTTP so it can be tested with `curl`
  independently of Open WebUI. Keep that property.
- The Pipe function is a thin client. Agent logic does not live in it.
- Memory is injected into the system prompt automatically each turn *and*
  exposed as a tool for on-demand queries. Both paths are intentional.
- Open WebUI's `__user__` ID is the Honcho peer ID. Do not generate our own.

## Local Notes

- Open WebUI runs in Docker; the agent service may run on the host during
  development. Use `host.docker.internal` for container-to-host calls.
- Honcho's embedding dimension is fixed in the pgvector schema at first run.
  Confirm the embedding model with me before anything touches the database.
