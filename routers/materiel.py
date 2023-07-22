from fastapi import APIRouter, Depends, status
import schemas
from database import get_db
from sqlalchemy.orm import Session
from repository import materiel
from typing import List
from oauth2 import get_current_user

router = APIRouter(
    prefix='/material',
    tags=['Materials']
)

@router.post('/new', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowMateriel)
def create(request : schemas.Materiel, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return materiel.create(request, db)

@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowMateriel])
def get_all(db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return materiel.get_all(db)

@router.get('/name/{name}', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowMateriel])
def search_material(name : str, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return materiel.search_name(name, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowMateriel)
def get_one(id : int, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return materiel.get_one(id, db)

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id : int, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return materiel.delete(id, db)

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Materiel, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return materiel.update(id, request, db)