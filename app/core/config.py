from typing import List
from decouple import config
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY', cast=str)
    ALGORITHM: str = "HS256" # info de seguranca
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [] # por enquanto vazio.
    PROJECT_NAME: str = 'FastToDo'

    # DATABASE
    MONGO_CONNECTION_STRING: str = config('MONGO_CONNECTION_STRING', cast=str)

    # classe para instanciar//
    class Config:
        case_sensitive = True

settings = Settings()