
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_route_factorielle():
    response = client.get("/factorielle/5")

    assert response.status_code == 200
    assert response.json() == {"n": 5, "resultat": 120}


def test_route_factorielle_negative():
    response = client.get("/factorielle/-1")

    assert response.status_code == 400
    assert response.json()["detail"] == "n doit être positif ou nul"
