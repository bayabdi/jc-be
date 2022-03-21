from sqlalchemy import Column, Integer, String
from db.models import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(250), unique=True)
    name = Column(String(250))
    surname = Column(String(250))
    hashed_password = Column(String(250))
    jobs = relationship("Job")
    
    def __repr__(self):
        return '<User: {}>'.format(self.id)