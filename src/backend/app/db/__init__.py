from fastapi import FastAPI

from .base import Base
from .session import engine
from db.models import * 

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield