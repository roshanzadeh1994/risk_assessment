from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Risk
from schemas import RiskCreate, RiskResponse
from typing import List
import asyncio
from db.models import Task

router = APIRouter(prefix="/risks", tags=["Risks"])


async def run_risk_workflow(risk_id: int, db: Session):
    # Zwei Aufgaben für das Risiko erstellen
    task1 = Task(risk_id=risk_id, assignee="Safety Officer", description="Erste Sicherheitsbewertung")
    task2 = Task(risk_id=risk_id, assignee="Team Leader", description="Teamüberprüfung")

    db.add_all([task1, task2])
    db.commit()

    await asyncio.sleep(10)

    risk = db.query(Risk).filter(Risk.id == risk_id).first()
    if risk:
        risk.status = "completed"
        db.commit()



# Dependency für Session-Erstellung
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post("/", response_model=RiskResponse)
def create_risk(
    risk: RiskCreate,
    background_tasks: BackgroundTasks, 
    db: Session = Depends(get_db)
    ):
    
    new_risk = Risk(
        title=risk.title,
        description=risk.description,
        category=risk.category
    )
    
    db.add(new_risk)
    db.commit()
    db.refresh(new_risk)
    
    # Starte den Workflow asynchron im Hintergrund
    background_tasks.add_task(run_risk_workflow, new_risk.id, db)
    
    return new_risk



@router.get("/", response_model=List[RiskResponse])
def get_all_risks(db: Session = Depends(get_db)):
    risks = db.query(Risk).all()
    return risks

@router.get("/{risk_id}", response_model=RiskResponse)
def get_risk_by_id(risk_id: int, db: Session = Depends(get_db)):
    risk = db.query(Risk).filter(Risk.id == risk_id).first()
    if not risk:
        raise HTTPException(status_code=404, detail="Risk not found")
    return risk
