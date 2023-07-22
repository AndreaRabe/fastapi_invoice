from datetime import date
from fastapi import HTTPException, status
import models, schemas
from hashing import Hash
from sqlalchemy.orm import Session

def create(request : schemas.Facture, db : Session):
    new_facture = models.Facture(
        ref_facture = request.ref_facture,
        date = request.date, 
        montant = request.montant,
        id_adresse = request.id_adresse)
    
    db.add(new_facture)
    db.commit()
    db.refresh(new_facture)
    return new_facture

def get_one(ref_facture : str, db : Session):
    facture = db.query(models.Facture).filter(models.Facture.ref_facture == ref_facture).first()
    if not facture:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invoice with reference : {ref_facture} not found')
    return facture

def get_all(db : Session):
    facture = db.query(models.Facture).all()
    return facture

# def delete(ref_facture : str, db : Session):
#     facture = db.query(models.Facture).filter(models.Facture.ref_facture == ref_facture)
#     if not facture.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invoice with reference : {ref_facture} not found')
#     facture.delete()
#     db.commit()
#     return 'Deleted successfully'

# def update(ref_facture : str, request : schemas.Facture, db : Session):
#     facture_data = dict(request) 
#     facture = db.query(models.Facture).filter(models.Facture.ref_facture == ref_facture)
#     if not facture.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invoice with reference : {ref_facture} not found')
#     facture.update(facture_data)
#     db.commit()
#     return 'Updated successfully'

def search_ref(ref_facture : str, db : Session):
    facture = db.query(models.Facture).filter(models.Facture.ref_facture == ref_facture).first()
    if not facture:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invoice with reference : {ref_facture} not found')
    return facture

def search_date(date : date, db : Session):
    facture = db.query(models.Facture).filter(models.Facture.date == date).all()
    if not facture:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invoice with reference : {date} not found')
    return facture