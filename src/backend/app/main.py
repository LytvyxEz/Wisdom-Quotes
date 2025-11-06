from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from db import lifespan
from api import quoutes_router, home_router

def init_app():
    
    app = FastAPI(title='Winsdom Quotes', lifespan=lifespan)

    app.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")
    app.include_router(quoutes_router)
    app.include_router(home_router)
    
    return app

app = init_app()