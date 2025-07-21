from datetime import datetime
from sqlmodel.sql.expression import desc
from sqlmodel.ext.asyncio.session import AsyncSession

from .models import Book
from .schemas import BookCreateModel
from sqlmodel import select


class BookService:
    async def get_all_books(self, session: AsyncSession):
        
        statement = select(Book).order_by(desc(Book.created_at))

        result = await session.exec(statement)

        return result.all()
    

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession) -> Book:
        new_book = Book(**book_data.dict())
        new_book.created_at = datetime.utcnow()
        new_book.edited_at = datetime.utcnow()

        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book
    
    async def get_book(self, book_uid: str, session: AsyncSession):

        statement = select(Book).where(Book.uid == book_uid)

        result = await session.exec(statement)

        book = result.first()

        return book if book is not None else None
    
    async def update_book(self, book_uid: str, update_data: BookCreateModel, session: AsyncSession):
        
        book_to_update = await self.get_book(book_uid, session)

        if book_to_update is not None:
            update_data_dict = update_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)
            
            await session.commit()

            return book_to_update
        
        return None
    
    async def delete_book(self, book_uid: str, session: AsyncSession):

        book_to_delete = await self.get_book(book_uid, session)
    
        if book_to_delete is not None:
            await session.delete(book_to_delete)

            await session.commit()

            return {}
        
        return None
    

