from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db
from typing import List
from app.schemas.option import OptionCreate, OptionResponse
from app.auth import get_current_user

router = APIRouter(prefix="/options", tags=["Options"])

@router.post("/", response_model=List[OptionResponse])
def create_option(
    option: schemas.option.OptionCreate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_option = models.Option(**option.dict())
    db.add(db_option)
    db.commit()
    db.refresh(db_option)
    return db_option

@router.get("/question/{question_id}", response_model=List[OptionResponse])
def get_options_by_question(
    question_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.Option).filter(models.Option.question_id == question_id).all()

@router.get("/", response_model=List[OptionResponse])
def list_options(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.Option).all()



@router.get("/{option_id}", response_model=OptionResponse)
def get_option(
    option_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    option = db.query(models.Option).filter(models.Option.id == option_id).first()
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")
    return option

@router.put("/{option_id}", response_model=OptionResponse)
def update_option(
    option_id: int, 
    option_update: OptionCreate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    option = db.query(models.Option).filter(models.Option.id == option_id).first()
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")

    for field, value in option_update.dict(exclude_unset=True).items():
        setattr(option, field, value)

    db.commit()
    db.refresh(option)
    return option

@router.delete("/{option_id}", status_code=204)
def delete_option(
    option_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    option = db.query(models.Option).filter(models.Option.id == option_id).first()
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")

    db.delete(option)
    db.commit()
    return