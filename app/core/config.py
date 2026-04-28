from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Application settings
    app_name: str = "FastAPI Service"
    app_version: str = "1.0.0"
    debug: bool = False

    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000

    # Database settings
    database_url: str = "postgresql://user:password@localhost/dbname"
    db_echo: bool = False

    # JWT settings
    secret_key: str = "your-secret-key-change-this"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS settings
    allowed_origins: list = ["http://localhost:3000", "http://localhost:8080"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
