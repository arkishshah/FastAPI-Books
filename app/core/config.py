from pydantic_settings import BaseSettings
from typing import List
from pathlib import Path
import os

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Books API"
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-for-development")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = f"sqlite:///{Path(__file__).parent.parent.parent}/books.db"
    
    # CORS Settings
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:8000",
        "http://localhost:3000"
    ]
    
    # Environment settings
    ENV: str = "development"
    LOG_LEVEL: str = "DEBUG"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()