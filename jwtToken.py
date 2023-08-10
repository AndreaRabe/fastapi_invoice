from datetime import timedelta, datetime
from jose import jwt, JWTError
import schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7fjksjefi5s7f7s54dffsffsgfsgs"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token : str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")  # Récupérer l'email depuis le token
        id_adresse: int = payload.get("adresse")  # Récupérer l'id_adresse depuis le token
        nom: str = payload.get("nom")
        id: int = payload.get("id")
        role : bool = payload.get("role")

        
        if email is None or id_adresse is None or nom is None or id is None or role is None:
            raise credentials_exception
            
        token_data = schemas.TokenData(email=email, id_adresse=id_adresse, id=id, nom=nom, role=role)  # Créer un objet TokenData avec les informations
    except JWTError:
        raise credentials_exception