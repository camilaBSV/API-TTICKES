"""
core/database.py
Conexión a MongoDB Atlas usando DATABASE_URL y COLECCION definidas en .env.
"""
import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.uri_parser import parse_uri

from app.core.config import settings

logger = logging.getLogger(__name__)

_client: MongoClient | None = None


def validate_database_url(database_url: str) -> str:
    """Valida que la URI de Mongo incluya el nombre de la base de datos."""
    if not database_url or not database_url.strip():
        raise ValueError("DATABASE_URL no está definido. Definí la variable en Render.")

    parsed = parse_uri(database_url)
    if not parsed.get("database"):
        raise ValueError(
            "DATABASE_URL debe incluir /<database-name>, por ejemplo: "
            "mongodb+srv://USER:PASS@cluster0.example.mongodb.net/soporte?appName=Cluster0"
        )

    return database_url


def get_client() -> MongoClient:
    global _client
    if _client is None:
        try:
            uri = validate_database_url(settings.DATABASE_URL)
            _client = MongoClient(uri, serverSelectionTimeoutMS=5000)
            # Verificar conexión
            _client.admin.command("ping")
            logger.info("Conexión a MongoDB Atlas establecida correctamente.")
        except (ConnectionFailure, ValueError) as e:
            logger.error(f"No se pudo conectar a MongoDB Atlas: {e}")
            raise
    return _client


def get_db():
    """Retorna la base de datos principal del cliente."""
    client = get_client()
    return client.get_default_database()


def get_collection():
    """Retorna la colección definida en la variable COLECCION (.env)."""
    db = get_db()
    return db[settings.COLECCION]


def close_connection():
    global _client
    if _client:
        _client.close()
        _client = None
        logger.info("Conexión a MongoDB Atlas cerrada.")
