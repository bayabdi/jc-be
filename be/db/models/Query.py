from sqlalchemy import Column, Integer, String
from db.models import Base

class Query(Base):
    __tablename__ = "query"
    
    id = Column(Integer, primary_key=True)
    text = Column(String(500))
    location = Column(String(500))
    
    def __repr__(self):
        return '<Query: {}>'.format(self.id)