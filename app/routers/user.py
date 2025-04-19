from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import db_dep, current_user_dep, admin_user_dep
from app.schemas import UserResponse, UserCreate, UserUpdate
from app.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/all/", response_model=list[UserResponse])
async def get_users(db: db_dep):
    return db.query(User).all()

@router.get("/{id}/", response_model=UserResponse)
async def get_user(id: int, db: db_dep):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    
    return user

@router.post("/create/", response_model=UserResponse)
async def create_user(
        user: UserCreate, 
        db: db_dep,
        current_user: current_user_dep
    ):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )
    
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=400,
            detail="Email already exists."
        )
    
    new_user = User(**user.dict())
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.put("/{id}/", response_model=UserResponse)
async def update_user(
        id: int, 
        user: UserUpdate, 
        db: db_dep,
        current_user: current_user_dep
    ):
    existing_user = db.query(User).filter(User.id == id).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    
    if user.email and db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=400,
            detail="Email already exists."
        )
    
    if user.username and db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=400,
            detail="Username already exists."
        )
    
    for key, value in user.dict(exclude_unset=True).items():
        setattr(existing_user, key, value)
    
    db.commit()
    db.refresh(existing_user)

    return existing_user

@router.patch("/{id}/")
async def patch_user(
        id: int, 
        user: UserUpdate, 
        db: db_dep,
        current_user: current_user_dep
    ):
    existing_user = db.query(User).filter(User.id == id).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    
    for key, value in user.dict(exclude_unset=True).items():
        setattr(existing_user, key, value)
    
    db.commit()
    db.refresh(existing_user)

    return existing_user

@router.delete("/{id}/")
async def delete_user(
        id: int, 
        db: db_dep,
        current_user: current_user_dep
    ):
    existing_user = db.query(User).filter(User.id == id).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    
    db.delete(existing_user)
    db.commit()

    return {"detail": "User deleted successfully."}

@router.get("/me/", response_model=UserResponse)
async def get_me(
        db: db_dep,
        current_user: current_user_dep
    ):
    return current_user