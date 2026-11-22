# Tests de la route /sante.
# Lancer tous les tests : pytest -v

from fastapi.testclient import TestClient

from app.main import app

# Client de test : il simule des requêtes vers l'API sans avoir à la lancer.
client = TestClient(app)


def test_sante():
    # On appelle la route /sante.
    r = client.get("/sante")
    # On vérifie que la réponse est OK (code 200)...
    assert r.status_code == 200
    # ...et que le contenu renvoyé est bien celui attendu.
    assert r.json() == {"statut": "ok"}