from pydantic import BaseModel
from datetime import datetime

class OptionBase(BaseModel):
    title: str
    is_correct: bool

class OptionCreate(OptionBase):
    question_id: int

class OptionResponse(OptionBase):
    id: int
    question_id: int
    created_at: datetime

    class Config:
        from_attributes = True