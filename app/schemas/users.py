# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birthdate: Optional[date] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    joined_at: datetime
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str