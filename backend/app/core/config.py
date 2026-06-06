# Pydantic Settings using SettingsConfigDict (v2)

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "venturescope"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
