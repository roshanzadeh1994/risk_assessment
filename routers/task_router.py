"""
API Router for managing tasks associated with risks.
"""

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Task
from schemas import TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# routers/task_router.py
@router.get("/{risk_id}/tasks", response_model=List[TaskResponse])
def get_tasks_for_risk(risk_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.risk_id == risk_id).all()
    return tasks
