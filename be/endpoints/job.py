from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .depends import get_db
from models import job
from core.security import auth_wrapper
import repositories.job
import repositories.user

router = APIRouter()

@router.post("/add", response_model=job.Job, dependencies=[Depends(auth_wrapper)])
def add(job: job.JobAdd, db: Session = Depends(get_db), email: str = Depends(auth_wrapper)):
    user = repositories.user.get_by_email(db, email)
    return repositories.job.add(db, job, user)

@router.get("/search", response_model= List[job.Job])
def get_jobs(text: str = '', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repositories.job.search(db, text, skip, limit)