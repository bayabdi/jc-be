from sqlalchemy.orm import Session
from db.models import User, Job, Query, Keyword
from models import job
from sqlalchemy import and_, or_
import math
from sqlalchemy.sql.expression import func
from googletrans import Translator
import unidecode

def add(db: Session, job: job.JobAdd, user: User):
    mid = db.query(func.max(Job.id)).scalar()
    
    translator = Translator()
    
    
    if job.link == '':
        if not mid:
            mid = 1
        else:
            mid += 1
        job.link = str(mid)
    
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
        user_id = user.id,
        deadline = job.deadline,
        title_en = translate(db, translator, job.title),
        description_en = translate(db, translator, job.description),
        category_en = translate(db, translator, job.category),
        requirement_en = translate(db, translator, job.requirement),
        company_name_en = translate(db, translator, job.company_name),
        company_description_en = translate(db, translator, job.company_description),
        location_en = translate(db, translator, job.location),
        salary_en = translate(db, translator, job.salary),
        language_en = translate(db, translator, job.language)
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    
    return db_job

def translate(db, translator, text):
    if text == '':
        return ''
    text = text.lower()
    trans_text = translator.translate(text, src='vi', dest='en').text.lower()

    if trans_text == text:
        text = unidecode.unidecode(text).lower()
        keyword = db.query(Keyword).filter(func.lower(Keyword.unaccented_text) == text).first()

        if (keyword == None):
            return text
        return keyword.text_en
        
    return trans_text
    
    
def edit(db: Session, job: job.JobEdit, user: User):
    db_job = db.query(Job).filter(and_(Job.id == job.id)).first()
    
    translator = Translator()
    
    if db_job != None:
        db_job.title = job.title,
        db_job.title_en = translate(db, translator, db_job.title),
        db_job.link = job.link,
        db_job.description = job.description,
        db_job.description_en = translate(db, translator, db_job.description),
        db_job.category = job.category,
        db_job.category_en = translate(db, translator, db_job.category),
        db_job.requirement = job.requirement,
        db_job.requirement_en = translate(db, translator, db_job.requirement),
        db_job.company_name = job.company_name,
        db_job.company_name_en = translate(db, translator, db_job.company_name),
        db_job.company_description = job.company_description,
        db_job.company_description_en = translate(db, translator, db_job.company_description),
        db_job.location = job.location,
        db_job.location_en = translate(db, translator, db_job.location),
        db_job.company_size = job.company_size,
        db_job.company_logo = job.company_logo,
        db_job.salary = job.salary,
        db_job.salary_en = translate(db, translator, db_job.salary),
        db_job.post_date = job.post_date,
        db_job.language = job.language,
        db_job.language_en = translate(db, translator, db_job.language),
    
    db.commit()
    
    return db_job

def delete(db: Session, id: int, user: User):
    db.query(Job).filter(and_(Job.id == id, Job.user_id == user.id)).delete()
    db.commit()

def search(db: Session, text: str, location: str, skip: int, take: int):
    db_query = Query(
        text = text.lower(),
        location = location
    )
    
    translator = Translator()
    
    text = func.lower(translate(db, translator, text))
    location = func.lower(translate(db, translator, location))
    
    if db.query(Query).filter(func.lower(Query.text) == db_query.text).count() < 1:
        db.add(db_query)
        db.commit()
    
    jobList = db.query(
        Job.id,
        Job.title,
        Job.link,
        Job.description,
        Job.category,
        Job.requirement,
        Job.company_name,
        Job.company_description,
        Job.location,
        Job.company_size,
        Job.company_logo,
        Job.salary,
        Job.post_date,
        Job.deadline,
        Job.language
    ).filter(
        and_(
            or_(
                func.lower(Job.title_en).like('%' + text + '%'),
                func.lower(Job.link).like('%' + text + '%'),
                func.lower(Job.description_en).like('%' + text + '%'),
                func.lower(Job.category_en).like('%' + text + '%'),
                func.lower(Job.requirement_en).like('%' + text + '%'),
                func.lower(Job.company_name_en).like('%' + text + '%'),
                func.lower(Job.company_description_en).like('%' + text + '%'),
                func.lower(Job.location_en).like('%' + text + '%'),
                func.lower(Job.company_size).like('%' + text + '%'),
                func.lower(Job.company_logo).like('%' + text + '%'),
                func.lower(Job.salary_en).like('%' + text + '%'),
                func.lower(Job.post_date).like('%' + text + '%'),
                func.lower(Job.language_en).like('%' + text + '%'),
            ),
            func.lower(Job.location_en).like('%' + location + '%'),
        )
    ).order_by(Job.id.desc()).offset(skip * take).limit(take).all()
    
    list = db.query(Job).filter(
        and_(
            or_(
                func.lower(Job.title_en).like('%' + text + '%'),
                func.lower(Job.link).like('%' + text + '%'),
                func.lower(Job.description_en).like('%' + text + '%'),
                func.lower(Job.category_en).like('%' + text + '%'),
                func.lower(Job.requirement_en).like('%' + text + '%'),
                func.lower(Job.company_name_en).like('%' + text + '%'),
                func.lower(Job.company_description_en).like('%' + text + '%'),
                func.lower(Job.location_en).like('%' + text + '%'),
                func.lower(Job.company_size).like('%' + text + '%'),
                func.lower(Job.company_logo).like('%' + text + '%'),
                func.lower(Job.salary_en).like('%' + text + '%'),
                func.lower(Job.post_date).like('%' + text + '%'),
                func.lower(Job.language_en).like('%' + text + '%'),
            ),
            func.lower(Job.location_en).like('%' + location + '%'),
        )
    ).all()
    
    result = job.JobPage(
        jobList = jobList,
        page = skip,
        totalPage = math.ceil(len(list) / take),
        hasNext = False
    )
    
    result.page += 1
    result.hasNext = (result.page < result.totalPage)
    
    return result

def get_by_link(db: Session, link: str):
    return db.query(Job).filter(Job.link == link).first()

def getById(db: Session, id: int):
    return db.query(Job).filter(
        Job.id == id
    ).first()