from fastapi import APIRouter, Depends, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from repository import adresse
from typing import List
from oauth2 import get_current_user

router = APIRouter(
    prefix='/adress',
    tags=['Address']
)

@router.post('/new', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowAdresse)
def create(request : schemas.Adresse, db : Session = Depends(get_db)):
    return adresse.create(request,db)

@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowAdresse])
def get_all(db : Session = Depends(get_db)):
    return adresse.get_all(db)

@router.get('/name/{name}', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowAdresse])
def search_user(name : str, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return adresse.search_name(name, db) 

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowAdresse)
def get_one(id : int, db : Session = Depends(get_db),):
    return adresse.get_one(id, db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Adresse, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return adresse.update(id, request, db)