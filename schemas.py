from pydantic import BaseModel, ConfigDict
from typing import Optional


# مدل برای دریافت داده هنگام ساخت ریسک
class RiskCreate(BaseModel):
    title: str
    description: str
    category: str


# مدل کامل برای پاسخ‌دهی (شامل id و status)
class RiskResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    status: str

    class RiskResponse(BaseModel):
        ...
        model_config = ConfigDict(from_attributes=True)


class TaskResponse(BaseModel):
    id: int
    risk_id: int
    assignee: str
    description: str

    model_config = ConfigDict(from_attributes=True)

