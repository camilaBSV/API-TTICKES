"""
core/config.py
Carga de variables de entorno y configuración central de la API.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL:str=" mongodb+srv://camilabsv24_db_user:6naSzOugf5wFflQV@cluster0.c3fenc0.mongodb.net/?appName=Cluster0"
    COLECCION: str
    SECRET_KEY: str = "supersecretkey2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
