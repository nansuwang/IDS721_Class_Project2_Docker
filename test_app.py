from os import path

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_necessary_files():
    assert path.exists("app.py")
    assert path.exists("klargest.py")


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
