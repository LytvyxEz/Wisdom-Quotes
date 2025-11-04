from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from services import gemini
from db.crud import crud_operations
from schemas import QuoteOutput
from uttils import logger, cleaner

import json


quoutes_router = APIRouter(prefix='/quotes')

quoutes_router.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")

templates = Jinja2Templates(directory="src/frontend/templates")


@quoutes_router.get('/random', response_model=QuoteOutput)
async def get_random_quote(
    request: Request,
    quote: str = Query(default=None), 
    author: str = Query(default=None), 
    explaining: str = Query(default=None),
    language: str = Query(default=None)
    ):
    
    response = await gemini.random_quote() if not language else await gemini.get_translated_quote({
        'quote': quote,
        'author': author,
        'explaining': explaining
    }, language)
    
    logger.info(response)
    cleaned_response = cleaner(response.strip())
    
    json_response = json.loads(cleaned_response)
    
    
    crud_operations.add_quote(
        quote=json_response['quote'], 
        author=json_response['author'], 
        explaining=json_response['explaining']
    )
    
    return templates.TemplateResponse(
        'quote.html',
        {
            'request': request,
            'response': json_response,
            'language': language,
            'is_translated': False if not language else True
        }
    )
