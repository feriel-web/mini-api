

from fastapi import FastAPI, HTTPException
from app.outils.math import factorielle

app = FastAPI(title="Mini API")


# Route de santé : permet de vérifier que l'API est bien en marche.
@app.get("/sante")
def sante():
    return {"statut": "ok"}

# Route factorielle : calcule la factorielle d'un nombre.
@app.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))
