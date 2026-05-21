from app.db.models.user_model import User

def get_user(db):
    users = db.query(User).all()

    return users

def create_user():
    return "User created successfully"