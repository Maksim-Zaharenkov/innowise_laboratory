from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import engine, session_local
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)