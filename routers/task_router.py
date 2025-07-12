from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Risk
from schemas import TaskResponse
from typing import List
from db.models import Task
from db.database import get_db


router = APIRouter(prefix="/tasks", tags=["Tasks"])




# routers/task_router.py
@router.get("/{risk_id}/tasks", response_model=List[TaskResponse])
def get_tasks_for_risk(risk_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.risk_id == risk_id).all()
    return tasks

