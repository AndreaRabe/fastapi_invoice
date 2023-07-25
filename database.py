from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = "bpxpc8kdjoej5f9hgp0r-mysql.services.clever-cloud.com"
port = 3306
username = "ue7a9vcndtwyaln8"
password = "votre_mot_de_passe"
database_name = "bpxpc8kdjoej5f9hgp0r"

# Créez la "Connection URI"
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}"# put here the name of your database here

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
