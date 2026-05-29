"""
core/database.py
Conexión a MongoDB Atlas usando DATABASE_URL y COLECCION definidas en .env.
"""
import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from app.core.config import settings

logger = logging.getLogger(__name__)

_client: MongoClient | None = None


def get_client() -> MongoClient:
    global _client
    if _client is None:
        try:
            _client = MongoClient(settings.DATABASE_URL, serverSelectionTimeoutMS=5000)
            # Verificar conexión
            _client.admin.command("ping")
            logger.info("Conexión a MongoDB Atlas establecida correctamente.")
        except ConnectionFailure as e:
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
