from jose import jwt
from fastapi import Security, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from .config import ACCES_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def encode_token(user_id):
    expires = datetime.utcnow() + timedelta(days=0, minutes= ACCES_TOKEN_EXPIRE_MINUTES)
    payload = {
        'exp': expires,
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    
    token = jwt.encode(
        payload,
        SECRET_KEY,
        ALGORITHM
    ) 
    
    return { 'token': token, 'expires': expires } 
    
def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code = 401, detail = 'Signature has expired')
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=401, detail='Invalid token')

def auth_wrapper(auth: HTTPAuthorizationCredentials = Security(security)):
    return decode_token(auth.credentials)