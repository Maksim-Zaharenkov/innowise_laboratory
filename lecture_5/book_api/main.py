from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, session_local
from models import Base, Book as DbBook
from schemas import Book

app = FastAPI()

#create tables
Base.metadata.create_all(bind=engine)

#create session object
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=Book)
async def add_book(book: Book, db: Session = Depends(get_db)) -> DbBook:
    db_book = DbBook(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=Book)
async def get_books(db: Session = Depends(get_db)) -> List[DbBook]:
    return db.query(DbBook).all()