from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date

# schemas for all models
class User(BaseModel):
    E_mail : str
    nom_utilisateur : str
    mot_de_passe : str
    id_adresse : Optional[int] = None
    role : Optional[bool] = None

class UserData(BaseModel):
    id : int
    E_mail : str
    nom_utilisateur : str
    class Config():
        orm_mode = True

class Facture(BaseModel):
    ref_facture: str
    date : date
    montant : float
    rano : float
    id_adresse : int

class FactureData(BaseModel):
    ref_facture: str
    date : date
    montant : float
    class Config():
        orm_mode = True

class Adresse(BaseModel):
    nom_adresse : str

class AdresseData(Adresse):
    id : int
    class Config():
        orm_mode = True

class Materiel(BaseModel):
    nom_materiel : str
    duree_utilisation : float
    nombre_kw : float
    id_user : int

class MaterielData(Materiel):
    id : int
    class Config():
        orm_mode = True

# schemas show models, modify for all routers

# i don't know if i need to put | None = None for all of list

class ShowUser(BaseModel):
    id : int
    nom_utilisateur : str
    user_adresse : Optional[AdresseData] = None
    id_adresse : Optional[int] = None
    user_materiel : List[MaterielData] = []
    montant_payer : Optional[float] = None
    montant_rano :  Optional[float] = None
    class Config():
        orm_mode = True

class ShowFacture(BaseModel):
    ref_facture : str
    date : date
    montant : float
    rano : float
    facture_adresse : AdresseData
    class Config():
        orm_mode = True

class ShowAdresse(BaseModel):
    id : int
    nom_adresse : str
    adresse_user : List[UserData] = []
    adresse_facture : List[FactureData] = []
    class Config():
        orm_mode = True

class ShowMateriel(BaseModel):
    id : int
    nom_materiel : str
    duree_utilisation : float
    nombre_kw : float
    montant: float
    materiel_user : UserData
    class Config():
        orm_mode = True

# token and authentification

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : Optional[str] = None



