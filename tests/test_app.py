from fastapi.testclient import TestClient
from pytemplates_fastapi.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello PyTemplates User!"


def test_hello():
    response = client.get("/hello?user=jacob")
    assert response.status_code == 200
    assert response.json() == "Hello jacob!"


def test_goodbye():
    response = client.get("/goodbye?user=jacob")
    assert response.status_code == 200
    assert response.json() == "Goodbye jacob!"


def test_whoami():
    response = client.get("/whoami")
    assert response.status_code == 200
    assert list(response.json().keys()) == ["host_name", "host_ip", "process_id"]
