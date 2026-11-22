

from fastapi import FastAPI

app = FastAPI(title="Mini API")


# Route de santé : permet de vérifier que l'API est bien en marche.
@app.get("/sante")
def sante():
    return {"statut": "ok"}