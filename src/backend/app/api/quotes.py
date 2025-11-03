from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from services import gemini
from db.crud import crud_operations
from schemas import QuoteOutput
from uttils import logger

import json

quoutes_router = APIRouter(prefix='/quotes')

quoutes_router.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")

templates = Jinja2Templates(directory="src/frontend/templates")

@quoutes_router.get('/random', response_model=QuoteOutput)
async def get_random_quote(request: Request):
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
    return templates.TemplateResponse(
        'quote.html',
        {'request': request,
         'response': json_response}
    )


    