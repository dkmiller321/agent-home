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


settings = Settings()
