from pydantic import BaseModel
from datetime import date


class UserSchema(BaseModel):
    id: int
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    username: str
    birthdate: date
    joined_at: date
    is_active: bool
    is_staff: bool
    is_superuser: bool


dummy_data = {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "birthdate": date(year=2000, month=1, day=1),
    "email": "email",
    "hashed_password": "password",
    "joined_at": date(year=2000, month=1, day=1),
    "is_active": True,
    "is_staff": False,
    "is_superuser": False,
}

user = UserSchema(**dummy_data)
user_dict = user.model_dump()
print(user_dict)
