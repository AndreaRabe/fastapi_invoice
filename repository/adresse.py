from fastapi import HTTPException, status
import models, schemas
from hashing import Hash
from sqlalchemy.orm import Session

def create(request : schemas.Adresse, db : Session):
    new_adresse = models.Adresse(
        nom_adresse = request.nom_adresse
    )

    db.add(new_adresse)
    db.commit()
    db.refresh(new_adresse)
    return new_adresse

def get_one(id : int, db : Session):
    adresse = db.query(models.Adresse).filter(models.Adresse.id == id).first()
    if not adresse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Address with id : {id} not found')
    return adresse

def get_all(db : Session):
    adresse = db.query(models.Adresse).all()
    return adresse

def update(id : int, request : schemas.Adresse, db : Session):
    adresse_data = dict(request)
    adresse = db.query(models.Adresse).filter(models.Adresse.id == id)
    if not adresse.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Address with id : {id} not found')
    adresse.update(adresse_data)
    db.commit()
    return 'Updated successfully'

def search_name(name : str, db : Session):
    adresse = db.query(models.Adresse).filter(models.Adressse.nom_adresse.ilike(f"%{name}%")).all()
    if not adresse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with this name : {name} not found')
    return adresse