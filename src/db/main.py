from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from ..config import Config

from ..books.models import Book

engine: AsyncEngine = create_async_engine(
    Config.DATABASE_URL,
    echo=True,
)

async def init_db():

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
