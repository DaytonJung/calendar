from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self
from pydantic import (
    PostgresDsn,
    computed_field,
)

class Settings(BaseSettings):
    
    PROJECT_NAME: str
    POSTGRES_NAME: str
    PROJECT_VERSION: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str


    
    model_config = SettingsConfigDict(
        env_file='../.env', 
        env_ignore_empty=True,
        extra='ignore'
        )


settings = Settings()

print(f"Project Name: {settings.PROJECT_NAME}")
print(f"Project Version: {settings.POSTGRES_SERVER}")  