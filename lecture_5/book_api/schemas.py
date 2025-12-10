"""It is orm shemas module"""

from typing import List
from pydantic import BaseModel

class BookBase(BaseModel):

    """This class with main parameters for adding operations"""

    title: str
    author: str
    year: int

class BookUpdate(BaseModel):

    """This class with main parameters for updating operations"""

    title: str
    author: str
    year: int

class Book(BookBase):

    """This class with id, it is main class"""

    id: int

    class Config:

        """This configuration class for work with orm"""

        from_attributes = True

class BookResponse(BaseModel):

    """This class can help return total count of books for using pagination"""

    total: int
    books: List[Book]
