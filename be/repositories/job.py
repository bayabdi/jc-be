from sqlalchemy.orm import Session
from db.models import User, Job
from models import job
from sqlalchemy import and_, or_

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

def edit(db: Session, job: job.JobEdit, user: User):
    db_job = db.query(Job).filter(and_(Job.id == job.id, Job.user_id == user.id)).first()
    
    db_job.title = job.title,
    db_job.link = job.link,
    db_job.description = job.description,
    db_job.category = job.category,
    db_job.requirement = job.requirement,
    db_job.company_name = job.company_name,
    db_job.company_description = job.company_description,
    db_job.location = job.location,
    db_job.company_size = job.company_size,
    db_job.company_logo = job.company_logo,
    db_job.salary = job.salary,
    db_job.post_date = job.post_date,
    db_job.language = job.language,
    
    db.commit()
    
    return db_job

def delete(db: Session, id: int, user: User):
    db.query(Job).filter(and_(Job.id == id, Job.user_id == user.id)).delete()
    db.commit()

def search(db: Session, text: str, skip: int, take: int):
    return db.query(Job).filter(
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