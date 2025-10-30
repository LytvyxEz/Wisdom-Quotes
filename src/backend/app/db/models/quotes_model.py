from ..base import Base

from sqlalchemy import String, Column, Integer

class QuotesORM(Base):
    __tablename__ = 'quotes'
    
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String, nullable=False)
    author = Column(String, nullable=False)
    explaining = Column(String, nullable=False)