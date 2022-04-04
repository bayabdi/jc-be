from enum import unique
from sqlalchemy import Column, Integer, String, ForeignKey
from db.models import Base
from sqlalchemy.orm import relationship
class Job(Base):
    __tablename__ = "job"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(500), unique=True)
    link = Column(String(500))
    description = Column(String(10000))
    category = Column(String(250))
    requirement = Column(String(10000))
    company_name = Column(String(500))
    company_description = Column(String(10000))
    location = Column(String(500))
    company_size = Column(String(500))
    company_logo = Column(String(500))
    salary = Column(String(250))
    post_date = Column(String(250))
    language = Column(String(500))
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    def __repr__(self):
        return '<Job: {}>'.format(self.id)