from sqlalchemy import Column, Integer, String
from db.models import Base

class Keyword(Base):
    __tablename__ = "keyword"
    
    id = Column(Integer, primary_key=True)
    unaccented_text = Column(String(500))
    text = Column(String(500))
    text_en = Column(String(500))
    
    def __repr__(self):
        return '<Keyword    : {}>'.format(self.id)