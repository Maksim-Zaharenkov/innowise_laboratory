from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_DATABASE_URL = 'sqlite:///./lecture_5/book_collection.db'

engine = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread': False})

session_local = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()