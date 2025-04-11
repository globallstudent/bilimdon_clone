from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.dependencies import get_db
from app.schemas.topic import TopicResponse, TopicCreate
from app.auth import get_current_user

router = APIRouter(prefix="/topics", tags=["Topics"])

@router.post("/", response_model=TopicResponse)
def create_topic(
    topic: schemas.topic.TopicCreate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    
    db_topic = models.Topic(**topic.dict())
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

@router.get("/", response_model=List[TopicResponse])
def list_topics(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.Topic).all()

@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic(
    topic_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic


@router.put("/{topic_id}", response_model=TopicResponse)
def update_topic(
    topic_id: int, 
    topic_update: TopicCreate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    for field, value in topic_update.dict(exclude_unset=True).items():
        setattr(topic, field, value)

    db.commit()
    db.refresh(topic)
    return topic


@router.delete("/{topic_id}", status_code=204)
def delete_topic(
    topic_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    db.delete(topic)
    db.commit()
    return
