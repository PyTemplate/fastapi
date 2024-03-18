from fastapi.testclient import TestClient

from pytemplates_fastapi.app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello PyTemplates User!"


def test_whoami():
    response = client.get("/whoami")
    assert response.status_code == 200
    assert list(response.json().keys()) == ["host_name", "host_ip", "process_id"]
