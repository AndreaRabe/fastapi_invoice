from datetime import timedelta
from fastapi import APIRouter, Depends, Form, HTTPException, status
from typing import List

from jwtToken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
import schemas, models
from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentification']
)


@router.post('/login', response_model=schemas.Token)
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    # Query the database to get the user with the provided email
    user = db.query(models.User).filter(models.User.E_mail == username).first()

    # Check if the user exists in the database
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials!!!')

    # Verify the password using the Hash.verify function
    if not Hash.verify(user.mot_de_passe, password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')

    # Create an access token with the user's email as the subject (sub)
    access_token = create_access_token(data={"sub": user.E_mail})

    # Return the access token along with the token type
    return schemas.Token(access_token=access_token, token_type="bearer")
