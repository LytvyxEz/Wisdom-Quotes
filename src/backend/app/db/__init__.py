from .base import Base
from .session import engine
from db.models import * 

def init_db():
    Base.metadata.create_all(bind=engine)
