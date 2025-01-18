from fastapi import APIRouter, Depends, Query, Response, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import Optional
from sse_starlette.sse import EventSourceResponse
from ....core.security import get_current_user
from ....core.database import get_db
from ....schemas.book import Book, BookCreate, BookUpdate, PaginatedBooks
from ....models.book import Book as BookModel
from ....models.user import User
from ....core.exceptions import BookNotFoundException
import asyncio
import json
from datetime import datetime

security = HTTPBearer()

router = APIRouter(tags=["books"])

@router.post(
    "/", 
    response_model=Book, 
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(security)]
)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new book"""
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get(
    "/", 
    response_model=PaginatedBooks,
    dependencies=[Depends(security)]
)
def read_books(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    page: int = Query(1, gt=0),
    size: int = Query(10, gt=0, le=100)
):
    """Retrieve books with pagination."""
    skip = (page - 1) * size
    total = db.query(BookModel).count()
    books = db.query(BookModel).offset(skip).limit(size).all()

    if not books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No books found for page {page} with size {size}."
        )

    return {
        "total": total,
        "items": books,
        "page": page,
        "size": size,
        "pages": (total + size - 1) // size
    }

@router.get(
    "/{book_id}", 
    response_model=Book,
    dependencies=[Depends(security)]
)
def read_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Retrieve a specific book by ID"""
    if book := db.query(BookModel).filter(BookModel.id == book_id).first():
        return book
    raise BookNotFoundException()

@router.put(
    "/{book_id}", 
    response_model=Book,
    dependencies=[Depends(security)]
)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a book"""
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise BookNotFoundException()
    
    for field, value in book.model_dump(exclude_unset=True).items():
        setattr(db_book, field, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete(
    "/{book_id}", 
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(security)]
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a book"""
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise BookNotFoundException()
    
    db.delete(db_book)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get(
    "/stream/updates",
    dependencies=[Depends(security)]
)
async def stream_updates(current_user: User = Depends(get_current_user)):
    """Stream real-time updates (SSE) with timeout."""
    async def event_generator(timeout: int = 300):  # 5-minute timeout
        while timeout > 0:
            data = {"timestamp": datetime.now().isoformat()}
            yield {
                "event": "update",
                "data": json.dumps(data)
            }
            await asyncio.sleep(5)
            timeout -= 5
        logger.info("SSE connection closed due to timeout.")

    return EventSourceResponse(event_generator())
