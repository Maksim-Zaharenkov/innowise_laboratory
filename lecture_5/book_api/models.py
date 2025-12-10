"""It is database models module"""

from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):

    """This class is model of table named books"""

    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable= False, index=True)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
