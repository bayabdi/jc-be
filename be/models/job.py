from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
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

class JobEdit(JobBase):
    id: int
    pass

class JobPage(BaseModel):
    jobList: object
    page: int
    totalPage: int
    hasNext: bool
    
class Job(JobBase):
    id: int
    link: str
    user_id: int
    class Config:
        orm_mode = True
    