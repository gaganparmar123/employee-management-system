from fastapi import FastAPI

from .db.database import Base, engine
from .api.v1.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
    
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Employee Management API Running"}