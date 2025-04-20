from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self
from pydantic import (
    PostgresDsn,
    computed_field,
)

class Settings(BaseSettings):
    
    PROJECT_NAME: str
    POSTGRES_DB: str
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

    # Database URL
    @computed_field
    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
        )

settings = Settings()