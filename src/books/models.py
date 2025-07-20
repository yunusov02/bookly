from datetime import datetime
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg


import uuid


class Book(SQLModel, table=True):
    
    __tablename__ = "books"

    uid:uuid.UUID = Field(
        pg.UUID,
        primary_key=True,
        unique=True,
        nullable=False
    )

    title: str
    author: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime = Field(
        sa_column=Field(
            Column(
                pg.TIMESTAMP, default=datetime.now()
            )
        )
    )
    
    edited_at: datetime = Field(
        sa_column=Field(
            Column(
                pg.TIMESTAMP, default=datetime.now()
            )
        )
    )


    def __repr__(self):
        return f"Book {self.title}"
    
