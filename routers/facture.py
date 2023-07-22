from datetime import date
from fastapi import APIRouter, Depends, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from repository import facture
from typing import List
from oauth2 import get_current_user

router = APIRouter(
    prefix='/invoice',
    tags=['Invoices']
)

@router.post('/new', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowFacture)
def create(request : schemas.Facture, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return facture.create(request, db)

@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowFacture])
def get_all(db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return facture.get_all(db)

@router.get('/reference/{reference}', status_code=status.HTTP_200_OK, response_model=schemas.ShowFacture)
def search_ref(reference : str, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return facture.search_ref(reference, db)

@router.get('/date/{date}', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowFacture])
def search_date(date : date, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return facture.search_date(date, db)

# @router.delete('/delete/{reference}', status_code=status.HTTP_204_NO_CONTENT)
# def delete(reference : str, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
#     return facture.delete(reference, db)

# @router.put('/update/{reference}', status_code=status.HTTP_202_ACCEPTED)
# def update(reference : str, request : schemas.Facture, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
#     return facture.update(reference, request, db)