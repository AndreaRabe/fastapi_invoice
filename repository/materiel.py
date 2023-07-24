from fastapi import HTTPException, status
import models, schemas
from hashing import Hash
from sqlalchemy.orm import Session
from function import price

def create(request : schemas.Materiel, db : Session):
    new_materiel = models.Materiel(
        nom_materiel = request.nom_materiel,
        duree_utilisation = request.duree_utilisation,
        nombre_kw = request.nombre_kw,
        id_user = request.id_user,
        montant = (request.nombre_kw*request.duree_utilisation*price)
    )
    db.add(new_materiel)
    db.commit()
    db.refresh(new_materiel)
    return new_materiel

def get_one(id : int, db : Session):
    materiel = db.query(models.Materiel).filter(models.Materiel.id == id).first()
    if not materiel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Material with id : {id} not found')
    return materiel

def get_all(db : Session):
    materiel = db.query(models.Materiel).all()
    return materiel

def delete(id : int, db : Session):
    materiel = db.query(models.Materiel).filter(models.Materiel.id == id)
    if not materiel.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Material with id : {id} not found')
    materiel.delete()
    db.commit()
    return 'Delete successfully'

def update(id : int, request : schemas.Materiel, db : Session):
    materiel_data = models.Materiel(
        nom_materiel = request.nom_materiel,
        duree_utilisation = request.duree_utilisation,
        nombre_kw = request.nombre_kw,
        # id_user = request.id_user, # if thik that the user id is not use
        montant = (request.nombre_kw*request.duree_utilisation*price)
    )
    materiel = db.query(models.Materiel).filter(models.Materiel.id == id)
    if not materiel.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Material with id : {id} not found')
    materiel.update(materiel_data)
    db.commit()
    return 'Update successfully'

def search_name(name : str, db : Session):
    materiel = db.query(models.Materiel).filter(models.Materiel.nom_materiel.ilike(f"%{name}%")).all()
    if not materiel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Material with name : {id} not found')
    return materiel
