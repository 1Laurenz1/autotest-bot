"""
Module for reading configuration and secret keys from .env.

Модуль для чтения конфигурации и секретных ключей из .env.
"""

from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


# Configuration class for loading environment variables
class Settings(BaseSettings):
    OPENAI_KEY: SecretStr
    
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
        extra="forbid" # prohibits any unnecessary variables in .env
    )

    
# Creating a settings object for import in other modules.
settings = Settings()