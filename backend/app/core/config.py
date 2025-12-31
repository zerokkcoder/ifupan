from pydantic_settings import BaseSettings
from typing import List, Union

class Settings(BaseSettings):
    PROJECT_NAME: str = "iFupan API"
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]

    # Database Settings
    MYSQL_SERVER: str = "localhost"
    MYSQL_USER: str = "ifupan"
    MYSQL_PASSWORD: str = "ifupan"
    MYSQL_DB: str = "ifupan"
    MYSQL_PORT: int = 3306

    class Config:
        case_sensitive = True

settings = Settings()
