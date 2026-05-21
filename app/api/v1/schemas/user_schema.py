from pydantic import BaseModel

class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    role: str

class UserResponse(UserCreate):
    id: int
    full_name: str
    email: str
    role: str
    is_active: bool
    created_at: str

    class Config:
        orm_mode = True
