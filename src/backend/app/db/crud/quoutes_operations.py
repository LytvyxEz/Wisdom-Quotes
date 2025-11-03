from sqlalchemy import select

from ..models import QuotesORM
from ..session import get_db 

from abc import ABC, abstractmethod

class AbstractQuotesCRUD(ABC):
    @staticmethod
    @abstractmethod
    def add_quote(self, quote, author, explaining):
        pass

        
class QuotesCRUD(AbstractQuotesCRUD):
    @staticmethod
    def add_quote(quote, author, explaining):
        
        with get_db() as db:
            new_quote = QuotesORM(quote=quote, author=author, explaining=explaining)
            
            db.add(new_quote)
            db.commit()
            db.refresh(new_quote)
            
            return new_quote
        
crud_operations = QuotesCRUD()