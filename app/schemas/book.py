# app/schemas/book.py
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    published_date: date
    summary: Optional[str] = None
    genre: str = Field(..., min_length=1, max_length=100)

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    author: Optional[str] = Field(None, min_length=1, max_length=255)
    published_date: Optional[date] = None
    summary: Optional[str] = None
    genre: Optional[str] = Field(None, min_length=1, max_length=100)

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True

class PaginatedBooks(BaseModel):
    total: int
    items: list[Book]
    page: int
    size: int
    pages: int
