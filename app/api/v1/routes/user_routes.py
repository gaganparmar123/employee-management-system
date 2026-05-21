from app.services import user_service
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return user_service.get_user(db)

@router.post("/users")
def create_user():
    return user_service.create_user()