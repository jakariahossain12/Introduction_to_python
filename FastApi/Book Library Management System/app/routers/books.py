from fastapi import APIRouter,Path,Query
from app.models.books import Book,UpdateBook

from fastapi.responses import JSONResponse

from app.services.books import (
    getAllBook,
    getSingleBook,
    createNewBook,
    sort_book,
    updateBook
)

router = APIRouter(prefix="/books",tags=["books"])

@router.get("")
def home():
    return getAllBook()

@router.get("/sort")
def sort_books(
    sort_by: str = Query(default="rating",description="Sort by pages or rating"),
    order: str = Query(default="asc",description="Sort order")
):
    return sort_book(sort_by,order)

@router.get("/id/{book_id}")
def singleBook(book_id : int = Path(...,description="ID of the book",example="1")):
    return getSingleBook(book_id)

@router.post("/create")
def createBook(book:Book):
    createNewBook(book)
    return JSONResponse(status_code=201,content={'message':"New book added"})

@router.put("/update/{book_id}")
def bookUpdate(book_id : int, book:UpdateBook):
    updateBook(book_id,book)
    return JSONResponse(status_code=200,content={'message':"New book update"})
