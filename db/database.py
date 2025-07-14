from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Pfad zur SQLite-Datenbankdatei
DATABASE_URL = "sqlite:///./risk_db.sqlite3"

# Engine erstellen
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session erstellen
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency für Session-Erstellung
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
