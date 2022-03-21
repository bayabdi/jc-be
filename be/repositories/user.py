from sqlalchemy.orm import Session
from db.models import User
from models import user
from core.security import get_password_hash

def get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create(db: Session, u: user.SignUp):
    db_user = User(
        name = u.name,
        surname = u.surname,
        email = u.email,
        hashed_password = get_password_hash(u.password),
        jobs = []
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user