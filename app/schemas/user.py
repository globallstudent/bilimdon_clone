from pydantic import BaseModel
from datetime import datetime


# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(unique=True)
#     hashed_password: Mapped[str] = mapped_column(String(128))
#     username: Mapped[str] = mapped_column(String(32), unique=True)
#     first_name: Mapped[str] = mapped_column(String(32), nullable=True)
#     last_name: Mapped[str] = mapped_column(String(32), nullable=True)
#     birthdate: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
#     joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
#     is_active: Mapped[bool] = mapped_column(default=True)
#     is_staff: Mapped[bool] = mapped_column(default=False)
#     is_superuser: Mapped[bool] = mapped_column(default=False)

#     owned_games: Mapped[List["Game"]] = relationship(back_populates="owner")
#     submissions: Mapped[List["Submission"]] = relationship(back_populates="owner")
#     participations: Mapped[List["Participation"]] = relationship(back_populates="user")

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    first_name: str = None
    last_name: str = None
    birthdate: str = None
    joined_at: datetime
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    email: str = None
    username: str = None
    first_name: str = None
    last_name: str = None
    birthdate: str = None
    is_active: bool = None
    is_staff: bool = None
    is_superuser: bool = None

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    first_name: str = None
    last_name: str = None
    birthdate: str = None

    class Config:
        from_attributes = True

class UserInDB(UserResponse):

    hashed_password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        from_attributes = True

class UserInDBUpdate(BaseModel):
    email: str = None
    username: str = None
    first_name: str = None
    last_name: str = None
    birthdate: str = None
    is_active: bool = None
    is_staff: bool = None
    is_superuser: bool = None

    class Config:
        from_attributes = True

class UserInDBResponse(BaseModel):
    id: int
    email: str
    username: str
    first_name: str = None
    last_name: str = None
    birthdate: str = None
    joined_at: datetime
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        from_attributes = True


class UserInDBUpdateResponse(BaseModel):
    id: int
    email: str
    username: str
    first_name: str = None
    last_name: str = None
    birthdate: str = None
    is_active: bool = None
    is_staff: bool = None
    is_superuser: bool = None

    class Config:
        from_attributes = True

