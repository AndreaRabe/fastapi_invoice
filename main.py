from fastapi import FastAPI
import models
from routers import user, authentification, adresse, facture, materiel

app =  FastAPI()

models.Base.metadata.create_all()


app.include_router(user.router)
app.include_router(authentification.router)
app.include_router(adresse.router)
app.include_router(materiel.router)
app.include_router(facture.router)

