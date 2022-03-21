from sqlalchemy.orm import Session
from db.models import User, Job
from models import job
from sqlalchemy import or_

def add(db: Session, job: job.JobAdd, user: User):
    db_job = Job(
        title = job.title,
        link = job.link,
        description = job.description,
        category = job.category,
        requirement = job.requirement,
        company_name = job.company_name,
        company_description = job.company_description,
        location = job.location,
        company_size = job.company_size,
        company_logo = job.company_logo,
        salary = job.salary,
        post_date = job.post_date,
        language = job.language,
        user_id = user.id
        
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    
    return db_job

def search(db: Session, text: str, skip: int, take: int):
    return db.query(Job, User).filter(
        or_(
            Job.title.like('%' + text + '%'),
            Job.link.like('%' + text + '%'),
            Job.description.like('%' + text + '%'),
            Job.category.like('%' + text + '%'),
            Job.requirement.like('%' + text + '%'),
            Job.company_name.like('%' + text + '%'),
            Job.company_description.like('%' + text + '%'),
            Job.location.like('%' + text + '%'),
            Job.company_size.like('%' + text + '%'),
            Job.company_logo.like('%' + text + '%'),
            Job.salary.like('%' + text + '%'),
            Job.post_date.like('%' + text + '%'),
            Job.language.like('%' + text + '%'),
        )
    ).offset(skip).limit(take).all()