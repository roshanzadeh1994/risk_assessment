from fastapi import FastAPI
from db.database import engine
from db.models import Base
from routers import homepage_router, risk_router 

app = FastAPI(title="Risk Assessment API", version="1.0")

# Register the router
app.include_router(risk_router.router)
app.include_router(homepage_router.router)

# Create database tables (only runs once at startup)
Base.metadata.create_all(bind=engine)

