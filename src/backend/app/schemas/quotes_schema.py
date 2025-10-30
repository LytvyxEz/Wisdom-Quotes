from pydantic import BaseModel

class QuoteOutput(BaseModel):
    quote: str
    author: str
    explaining: str
