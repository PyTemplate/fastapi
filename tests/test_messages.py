import pytest

from fastapi.testclient import TestClient
from pytemplates_fastapi.app.main import app


def test_create():
    with TestClient(app) as client:
        response = client.post("/messages/", json={"content": "hello"})
        assert response.status_code == 201
        response2 = client.post("/messages/", json={"content": "hello again"})
        assert response2.status_code == 201


@pytest.mark.parametrize("id_number,status_code", [(1, 200), (2, 200), (100, 404)])
def test_read(id_number, status_code):
    with TestClient(app) as client:
        response = client.get(
            f"/messages?id_number={id_number}",
        )
        assert response.status_code == status_code


def test_readall():
    with TestClient(app) as client:
        response = client.get("/messages")
        assert response.status_code == 200


@pytest.mark.parametrize("id_number,status_code", [(1, 202), (100, 404)])
def test_update(id_number, status_code):
    with TestClient(app) as client:
        response = client.patch(f"/messages/{id_number}", json={"content": "goodbye"})
        assert response.status_code == status_code


@pytest.mark.parametrize("id_number,status_code", [(1, 202), (2, 202), (100, 404)])
def test_delete(id_number, status_code):
    with TestClient(app) as client:
        response = client.delete(
            f"/messages/{id_number}",
        )
        assert response.status_code == status_code
