from pydantic import (
    Field
)

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    project_title: str = "Vehicule Management SERVICE"
    project_description: str = "REST API service for Vehicule Management Application"
    project_version: str = "v0.0.1"

    API_V1_STR: str = "/api/v1"

    
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
