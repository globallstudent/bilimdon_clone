from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .option import OptionResponse

class QuestionBase(BaseModel):
    title: str
    description: Optional[str] = None
    topic_id: int

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    options: List[OptionResponse] = []

    class Config:
        from_attributes = True