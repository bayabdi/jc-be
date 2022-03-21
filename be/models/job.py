from pydantic import BaseModel
from .user import User
class JobBase(BaseModel):
    id: int
    title: str
    link: str
    description: str
    category: str
    requirement: str
    company_name: str
    company_description: str
    location: str
    company_size: str
    company_logo: str
    salary: str
    post_date: str
    language: str
    
class JobAdd(JobBase):
    pass

class Job(JobBase):
    user_id: int
    user: User
    class Config:
        orm_mode = True
    