from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from services import gemini
from db.crud import crud_operations
from schemas import QuoteOutput
from uttils import logger

import json

quoutes_router = APIRouter(prefix='/quotes')


@quoutes_router.get('/random', response_model=QuoteOutput)
async def get_random_quote():
    response = gemini.random_quote()
    logger.info(response)
    
    cleaned_response = response.strip()
    if cleaned_response.startswith('```'):
        cleaned_response = cleaned_response.split('\n', 1)[1]
        cleaned_response = cleaned_response.rsplit('```', 1)[0]
        cleaned_response = cleaned_response.strip()
    
    logger.info(cleaned_response)
    json_response = json.loads(cleaned_response)
    crud_operations.add_quote(quote=json_response['quote'], author=json_response['author'], explaining=json_response['explaining'])
    return json_response
