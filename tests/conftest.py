import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.models import Base
from main import app
from routers.risk_router import get_db

# --- Setup ---
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# --- Dependency override ---
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# --- Fixture ---
@pytest.fixture(scope="session")
def test_client():
    client = TestClient(app)
    yield client

    # Aufräumen nach allen Tests
    time.sleep(1)  # Kurze Pause, damit alle Verbindungen geschlossen werden
    try:
        os.remove("test.db")
    except PermissionError:
        print("⚠️ Cannot delete test.db - file still in use.")
    except FileNotFoundError:
        pass
