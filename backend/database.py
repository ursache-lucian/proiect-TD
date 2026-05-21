# database.py - Configurarea conexiunii la baza de date PostgreSQL (Supabase)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string catre baza de date Supabase
DATABASE_URL = "postgresql://postgres:AndreiIustin27@db.kjfpiwakkzntggxlwetb.supabase.co:5432/postgres"

# Cream motorul SQLAlchemy — fara connect_args, acela era doar pentru SQLite
engine = create_engine(DATABASE_URL)

# SessionLocal este clasa din care vom crea sesiuni de lucru cu BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base este clasa de baza pe care o vor mosteni toate modelele noastre
Base = declarative_base()

# Functie utila folosita in rute pentru a obtine o sesiune
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()