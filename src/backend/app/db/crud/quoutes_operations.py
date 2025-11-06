from sqlalchemy import select
from ..models import QuotesORM
from ..session import get_db
from abc import ABC, abstractmethod

class AbstractQuotesCRUD(ABC):
    @staticmethod
    @abstractmethod
    async def add_quote(quote: str, author: str, explaining: str):
        pass


class QuotesCRUD(AbstractQuotesCRUD):
    @staticmethod
    async def add_quote(quote: str, author: str, explaining: str):
        async with get_db() as db:
            new_quote = QuotesORM(
                quote=quote,
                author=author,
                explaining=explaining
            )

            db.add(new_quote)
            await db.commit()
            await db.refresh(new_quote)

            return new_quote
        
    @staticmethod
    async def get_all_quotes():
        async with get_db() as db:
            result = await db.execute(select(QuotesORM))
            return result.scalars().all()


crud_operations = QuotesCRUD()
