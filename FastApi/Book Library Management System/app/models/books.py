from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Optional,Literal

class Book(BaseModel):
    book_id : Annotated[int,Field(...,description="ID",examples=['1','2'])]
    title : Annotated[str,Field(...,description="Title of the book")]
    author : Annotated[str,Field(...,description="Author name of the book")]
    genre : Annotated[Literal["fiction", "science", "history", "biography","love"],Field(...,description="Genre of the author")]
    pages : Annotated[int,Field(...,description="Total number of book page")]
    rating : Annotated[float,Field(...,description="Rating of the book")]



class UpdateBook(BaseModel):
    title: Annotated[Optional[str], Field(None, description="Title of the book")]
    author: Annotated[Optional[str], Field(None, description="Author name of the book")]
    genre: Annotated[Optional[Literal["fiction", "science", "history", "biography","love"]], Field(None, description="Genre of the author")]
    pages: Annotated[Optional[int], Field(None, description="Total number of book page")]
    rating: Annotated[Optional[float], Field(None, description="Rating of the book")]