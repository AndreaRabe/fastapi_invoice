from datetime import date
from fastapi import HTTPException, status
import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from function import payed

def create(request : schemas.Facture, db : Session):
    try:
        new_facture = models.Facture(
            ref_facture = request.ref_facture,
            date = request.date, 
            montant = request.montant,
            rano = request.rano,
            id_adresse = request.id_adresse)
        
        db.add(new_facture)
        db.commit()
        payed(request.id_adresse, request.montant, request.rano, db)
        db.refresh(new_facture)
        return new_facture
    
    except IntegrityError as e:
        # Handle IntegrityError exception
        print("Integrity Error: Duplicate entry for primary key")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate entry for primary key")

    except Exception as e:
        # Handle other exceptions
        print("Unexpected Error:", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


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