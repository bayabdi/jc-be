from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str

class Auth(BaseModel):
    email: str
    password: str
    
class SignUp(Auth):
    name: str
    surname: str