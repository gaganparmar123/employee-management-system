from app.services import user_service
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.schemas import user_schema

router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return user_service.get_user(db)

@router.post("/users")
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)