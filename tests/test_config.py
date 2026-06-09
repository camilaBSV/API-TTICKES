import pytest
from unittest.mock import MagicMock, patch

from app.core import database
from app.core.database import close_connection, get_client, get_collection, validate_database_url


def test_validate_database_url_requires_db_name():
    with pytest.raises(ValueError, match="database name"):
        validate_database_url("mongodb+srv://user:pass@cluster0.example.mongodb.net/?appName=Cluster0")


def test_validate_database_url_accepts_database_name():
    uri = "mongodb+srv://user:pass@cluster0.example.mongodb.net/soporte?appName=Cluster0"

    assert validate_database_url(uri) == uri


def test_validate_database_url_rejects_invalid_scheme():
    with pytest.raises(ValueError, match="URI de MongoDB"):
        validate_database_url("https://example.com/soporte")


def test_get_client_and_close_connection():
    fake_client = MagicMock()
    fake_client.admin.command.return_value = None

    with patch("app.core.database.settings.DATABASE_URL", "mongodb+srv://user:pass@cluster0.example.mongodb.net/soporte?appName=Cluster0"), \
         patch("app.core.database._client", None), \
         patch("app.core.database.MongoClient", return_value=fake_client) as mongo_client:
        client = get_client()

    assert client is fake_client
    mongo_client.assert_called_once()
    fake_client.admin.command.assert_called_once_with("ping")

    close_connection()

    assert database._client is None


def test_get_collection_uses_placeholder_when_database_name_is_missing():
    with patch("app.core.database.settings.DATABASE_URL", "mongodb+srv://user:pass@cluster0.example.mongodb.net/?appName=Cluster0"):
        collection = get_collection()

    with pytest.raises(ValueError, match="database name"):
        collection.some_operation()


def test_get_collection_uses_real_collection_when_database_name_exists():
    fake_db = MagicMock()
    fake_db.__getitem__.return_value = "coleccion-mock"

    with patch("app.core.database.settings.DATABASE_URL", "mongodb+srv://user:pass@cluster0.example.mongodb.net/soporte?appName=Cluster0"), \
         patch("app.core.database.get_db", return_value=fake_db):
        collection = get_collection()

    assert collection == "coleccion-mock"
    fake_db.__getitem__.assert_called_once_with("colecciontest0")
