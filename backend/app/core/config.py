"""Configuration and settings for the FastAPI application."""

import os
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # App
    app_name: str = "Linked"
    app_version: str = "0.1.0"
    debug: bool = os.getenv("DEBUG", "True").lower() == "true"

    # Database
    database_url: str = "sqlite:///./linked.db"
    # For PostgreSQL migration: "postgresql://user:password@localhost/linked"
    echo_sql: bool = os.getenv("ECHO_SQL", "False").lower() == "true"

    # Security
    secret_key: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-prod")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # API
    api_v1_prefix: str = "/api/v1"
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    # External APIs
    linkedin_api_key: Optional[str] = os.getenv("LINKEDIN_API_KEY")
    gmail_api_key: Optional[str] = os.getenv("GMAIL_API_KEY")

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
