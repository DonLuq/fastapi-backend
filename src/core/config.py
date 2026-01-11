from typing import List, Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # API Configuration
    app_name: str = "FastAPI Application Default Name"
    api_key: Optional[str] = None

    # Finnhub API
    finnhub_email: Optional[str] = Field(default=None, alias="FINNHUB_EMAIL")
    finnhub_api_key: Optional[str] = Field(default=None, alias="FINNHUB_API_KEY")

    # Database
    storage_database_url: Optional[str] = Field(
        default=None, alias="STORAGE_DATABASE_URL"
    )
    storage_database_user: Optional[str] = Field(
        default=None, alias="STORAGE_DATABASE_USER"
    )
    storage_database_password: Optional[str] = Field(
        default=None, alias="STORAGE_DATABASE_PASSWORD"
    )

    # Logging
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    debug_mode: bool = Field(default=False, alias="DEBUG_MODE")

    # Storage
    storage_backend: str = "local"
    upload_dir: str = "/tmp/uploads"

    # CORS
    cors_origins: List[str] = ["*"]

    # Configuration for loading from environment variables
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, env_prefix=""
    )


settings = Settings()
