from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

home_router = APIRouter()

home_router.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")

templates = Jinja2Templates(directory="src/frontend/templates")

@home_router.get('/')
async def home(request: Request):
    return templates.TemplateResponse(
        'main.html',
        {'request': request}
    )