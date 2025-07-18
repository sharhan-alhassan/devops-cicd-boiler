from pydantic_settings import BaseSettings
from typing import List
import os
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "Backend Service"
    API_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Database
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Email
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_PORT: int = int(os.getenv("MAIL_PORT", 587))
    MAIL_SERVER: str = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_FROM_NAME: str = os.getenv("MAIL_FROM_NAME")

    MAIL_STARTTLS: bool = (os.getenv("MAIL_STARTTLS"),)
    MAIL_SSL_TLS: bool = (os.getenv("MAIL_SSL_TLS"),)
    USE_CREDENTIALS: bool = (os.getenv("USE_CREDENTIALS"),)
    VALIDATE_CERTS: bool = os.getenv("VALIDATE_CERTS")

    @property
    def DATABASE_URL(self) -> str:
        if os.getenv("ENVIRONMENT") == "production":
            connection_string = os.getenv("DATABASE_URL")
            if not connection_string:
                raise ValueError("DATABASE_URL environment variable is not set.")
            return connection_string
            # return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return "sqlite+aiosqlite:///./devops.db"

    # JWT
    SECRET_KEY: str = "Mc5aGOo3kRXK1jHCfG5SWDRwR5cfEnnP"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

    # CORS
    ALLOWED_HOSTS: List[str] = ["*"]

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = [
        "*",
        "http://localhost",
        "http://localhost:8080",
        "http://devops.tamale.forward.tiaspaces.com",
        "https://devops.tamale.forward.tiaspaces.com",
    ]

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra fields without validation errors -- to allow docker compose db splitted


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
