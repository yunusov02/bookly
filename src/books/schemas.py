from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdate(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str