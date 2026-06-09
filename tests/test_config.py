import pytest

from app.core.database import validate_database_url


def test_validate_database_url_requires_db_name():
    with pytest.raises(ValueError, match="database name"):
        validate_database_url("mongodb+srv://user:pass@cluster0.example.mongodb.net/?appName=Cluster0")
