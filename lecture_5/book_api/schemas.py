from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

    class Config:
        orm_mode = True  