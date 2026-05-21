from app.db.models.user_model import User

def get_user(db):
    users = db.query(User).all()

    return users

def create_user(db, user):
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user