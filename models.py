from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "Utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    E_mail = Column(String(100))
    nom_utilisateur = Column(String(100))
    mot_de_passe = Column(String(200))
    montant_payer = Column(Float) # from invoice
    montant_rano = Column(Float)
    role = Column(Boolean, default=0) # 0 if an user and 1 if an admin
    id_adresse = Column(Integer, ForeignKey("Adresses.id"), nullable=True, default=None)
    
    user_adresse = relationship("Adresse", back_populates="adresse_user")
    user_materiel = relationship("Materiel", back_populates="materiel_user")


class Facture(Base):
    __tablename__ = "Factures"
    ref_facture = Column(String(150), primary_key=True, index=True)
    date = Column(Date)
    montant = Column(Float)
    rano = Column(Float)
    id_adresse = Column(Integer, ForeignKey("Adresses.id"))

    facture_adresse = relationship("Adresse", back_populates="adresse_facture")

class Adresse(Base):
    __tablename__ = "Adresses"
    id = Column(Integer, primary_key=True, index=True)
    nom_adresse = Column(String(100))

    adresse_user = relationship("User", back_populates="user_adresse")
    adresse_facture = relationship("Facture", back_populates="facture_adresse")

class Materiel(Base):
    __tablename__ = "Materiels"
    id = Column(Integer, primary_key=True, index=True)
    nom_materiel = Column(String(100))
    duree_utilisation = Column(Float)
    nombre_kw = Column(Float)
    montant = Column(Float)
    id_user = Column(Integer, ForeignKey("Utilisateurs.id"))

    materiel_user = relationship("User", back_populates="user_materiel")
