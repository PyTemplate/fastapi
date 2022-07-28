import os
from pathlib import Path

import pytest

from pytemplates_fastapi.db.session import session


@pytest.fixture(autouse=True)
def mock_db_connection(monkeypatch):
    test_db_path = os.path.join(str(Path(__file__).parent), "test_database.json")
    monkeypatch.setattr(session, "filename", test_db_path)
