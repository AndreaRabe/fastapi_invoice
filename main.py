from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import user, authentification, adresse, facture, materiel

app =  FastAPI()

models.Base.metadata.create_all(bind = engine)

## add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
app.include_router(user.router)
app.include_router(authentification.router)
app.include_router(adresse.router)
app.include_router(materiel.router)
app.include_router(facture.router)

