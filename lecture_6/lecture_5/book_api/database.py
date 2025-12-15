"""It is database connection module"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

file_path = os.path.join(os.path.dirname(os.getcwd()), "book_collection.db")

SQL_DATABASE_URL = 'sqlite:///' + file_path

engine = create_engine(SQL_DATABASE_URL, connect_args={'check_same_thread': False})

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
