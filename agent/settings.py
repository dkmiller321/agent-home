"""Application settings, read once at startup."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-backed configuration.

    `extra="ignore"` matters: .env also carries Honcho, Postgres and Open WebUI
    variables that are not ours, and pydantic-settings rejects unknown fields by
    default.
    """

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openrouter_api_key: str
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    agent_model: str

    agent_host: str = "0.0.0.0"
    agent_port: int = 8080
    log_level: str = "INFO"

    honcho_base_url: str = "http://honcho:8000"
    # Empty is correct while AUTH_USE_AUTH is false: the SDK sends no
    # Authorization header when this is falsy.
    honcho_api_key: str = ""
    honcho_workspace_id: str = "agent-home"
    # The peer our own replies are attributed to. Fixed, unlike the user peer,
    # which arrives per request as Open WebUI's user ID.
    honcho_assistant_peer_id: str = "assistant"


settings = Settings()
