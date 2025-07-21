from sqlmodel import create_engine, text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import Config
from ..books.models import Book



async_engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)  # core connection object that
    # 1. translate ORM into SQL statement
    # 2. Sends those statements to the database
    # 3. Handles transactions


AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def init_db():
    """create a connection to our db"""

    async with async_engine.begin() as conn:
        # statement = text("select 'Hello World'")

        # result = await conn.execute(statement)

        # print(result)

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
