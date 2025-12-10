"""It is API module"""

from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, session_local
from models import Base, Book as BookModel
from schemas import Book, BookBase, BookUpdate, BookResponse

app = FastAPI()

#create tables
Base.metadata.create_all(bind=engine)

def get_db():
    """This method create session object"""
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=Book)
async def add_book(
    book: BookBase,
    db: Session = Depends(get_db)
    ):

    """This endpoint for add book in database"""

    db_book = BookModel(title=book.title, author=book.author, year=book.year)

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return Book.model_validate(db_book)

@app.get("/books/", response_model=BookResponse)
async def get_books(
    skip: int = Query(0),
    limit: int = Query(10),
    db: Session = Depends(get_db)
    ):

    """This endpoint for get list of books from database"""

    query = db.query(BookModel)
    total = query.count()
    books = query.offset(skip).limit(limit).all()

    return BookResponse(total=total, books=books)

@app.delete("/books/{book_id}", response_model=dict)
async def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
    ):

    """This endpoint for delete book from database"""

    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"detail": "Book deleted successfully"}

@app.put("/books/{book_id}", response_model=dict)
async def update_book(
    book_id: int,
    updated_book: BookUpdate,
    db: Session = Depends(get_db)
    ):

    """This endpoint for update book in database"""

    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = updated_book.title
    book.author = updated_book.author
    book.year = updated_book.year
    db.commit()

    return {"detail": "Book updated successfully", "book_id": book_id}

@app.get("/books/search/", response_model=BookResponse)
async def search_books(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    skip: int = Query(0),
    limit: int = Query(10),
    db: Session = Depends(get_db)
    ):

    """This endpoint for get list of books from database by parameters"""

    query = db.query(BookModel)

    if title:
        query = query.filter(BookModel.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(BookModel.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(BookModel.year == year)

    total = query.count()
    books = query.offset(skip).limit(limit).all()

    return BookResponse(total=total, books=books)
