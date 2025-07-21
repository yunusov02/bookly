from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

from src.db.main import init_db


version = 'v1'

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    print("Server is stopping")

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version= version,
    lifespan=lifespan
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])

