"""
core/config.py
Carga de variables de entorno y configuración central de la API.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = Field(
        default="",
        description="MongoDB Atlas URI. En Render debe incluir /<database-name>.",
    )
    COLECCION: str = "colecciontest0"
    SECRET_KEY: str = Field(default="cambie-este-secreto-en-render", min_length=16)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
