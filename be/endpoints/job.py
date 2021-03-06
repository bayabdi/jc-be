from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .depends import get_db
from models import job
from core.security import auth_wrapper
import repositories.job
import repositories.user

router = APIRouter()

@router.post("/add", response_model=job.Job, dependencies=[Depends(auth_wrapper)])
def add(job: job.JobAdd, db: Session = Depends(get_db), email: str = Depends(auth_wrapper)):
    if job.link != '':
        model = repositories.job.get_by_link(db, job.link)
        if model != None:
            raise HTTPException(status_code = 409, detail = 'Link is taken')
    
    user = repositories.user.get_by_email(db, email)
    return repositories.job.add(db, job, user)

@router.post("/edit", dependencies=[Depends(auth_wrapper)])
def edit(job: job.JobEdit, db: Session = Depends(get_db), email: str = Depends(auth_wrapper)):
    model = repositories.job.get_by_link(db, job.link)
    if model and model.id != job.id:  
        raise HTTPException(status_code = 409, detail = 'Link is taken')
    
    user = repositories.user.get_by_email(db, email)
    return repositories.job.edit(db, job, user)

@router.get("/delete", status_code=201)
def delete(id: int, db: Session = Depends(get_db), email: str = Depends(auth_wrapper)):
    user = repositories.user.get_by_email(db, email)
    repositories.job.delete(db, id, user)    

@router.get("/search")
def get_jobs(text: str = '', location: str = '', skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repositories.job.search(db, text, location, skip, limit)

@router.get("/get")
def get_job(id: int, db: Session = Depends(get_db)):
    return repositories.job.getById(db, id)