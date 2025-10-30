from fastapi import FastAPI

from api import quoutes_router

app = FastAPI()

app.include_router(quoutes_router)
