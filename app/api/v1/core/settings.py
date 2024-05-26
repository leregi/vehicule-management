from pydantic import (
    Field
)

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    project_title: str = "Vehicule Management SERVICE"
    project_description: str = "REST API service for Vehicule Management Application"
    project_version: str = "v0.0.1"

    API_V1_STR: str = "/api/v1"

    DATABASE_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str


    
    model_config = SettingsConfigDict(env_file=('.env/development/database',".env/development/web"), env_file_encoding="utf-8",extra='ignore')


settings = Settings()
