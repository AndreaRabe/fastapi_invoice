from fastapi import Depends, HTTPException, status
from models import User, Facture, Materiel
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db

price = 160  # price of kw in ariary

def payed(id_adresse: int, facture_montant: float, rano : float, db : Session = Depends(get_db)):
    montant_materiels_par_utilisateur = db.query(User.nom_utilisateur, func.sum(Materiel.montant))\
        .join(Facture, User.id_adresse == Facture.id_adresse)\
        .join(Materiel, User.id == Materiel.id_user)\
        .filter(Facture.id_adresse == id_adresse)\
        .group_by(User.nom_utilisateur)\
        .all()

    total_montant_materiels = sum(montant for _, montant in montant_materiels_par_utilisateur)
    nombre_utilisateurs = len(montant_materiels_par_utilisateur)

    rano_vola = rano/nombre_utilisateurs

    if facture_montant == total_montant_materiels:
        montant_plus = 0.0
    
    elif facture_montant > total_montant_materiels:
        reste = (facture_montant - total_montant_materiels) / nombre_utilisateurs
        montant_plus = reste

    elif facture_montant < total_montant_materiels:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect invoice value")

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="I am looking for an unpaid invoice")
    
    for nom, montant_materiels in montant_materiels_par_utilisateur:
        user = db.query(User).filter_by(nom_utilisateur=nom).first()
    
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user.montant_payer = montant_materiels + montant_plus
        user.montant_rano = rano_vola
    db.commit()



# frontend fonction to put null the value in column montant_payer for one user

def after_payed(id : int, db : Session = Depends(get_db)):
    user_data = User(montant_payer=None)
    user = db.query(User).filter(User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.update(user_data)
    db.commit()
    return 'Invoice Payed'
