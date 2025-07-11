from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Risk(Base):
    __tablename__ = "risks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    status = Column(String, default="in process")
    
    # Beziehung zu Tasks (Aufgaben), mit Kaskadierung beim Löschen
    tasks = relationship("Task", back_populates="risk", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    risk_id = Column(Integer, ForeignKey("risks.id"))
    assignee = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # Beziehung zurück zu Risk
    risk = relationship("Risk", back_populates="tasks")
