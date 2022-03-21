from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .depends import get_db
from models import user
import repositories.user
from core.security import verify_password, encode_token, auth_wrapper

router = APIRouter()

@router.post("/signup", status_code=201)
def signup(model: user.SignUp, db: Session = Depends(get_db)):
    if repositories.user.get_by_email(db, model.email):  
        raise HTTPException(status_code = 400, detail = 'Email is taken')
    repositories.user.create(db, model)
    
    return encode_token(model.email)

@router.post("/login", status_code=201)
def login(model: user.Auth, db: Session = Depends(get_db)):
    user = repositories.user.get_by_email(db, model.email)
    
    if (user is None) or (not verify_password(model.password, user.hashed_password)):
        raise HTTPException(status_code = 401, detail = "Invalid email and/or password")
    return encode_token(user.email)   

@router.get('/protected', dependencies=[Depends(auth_wrapper)])
def protected(username=Depends(auth_wrapper)):
    return { 'name': username }