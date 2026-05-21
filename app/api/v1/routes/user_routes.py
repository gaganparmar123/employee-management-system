from app.services import user_service
from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
def create_user():
    return user_service.create_user()