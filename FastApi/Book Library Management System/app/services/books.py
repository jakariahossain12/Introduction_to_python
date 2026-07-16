import mysql.connector
from fastapi import HTTPException,Path


from app.database import load_data,save_data,cursor,connection
from app.models.books import Book,UpdateBook

# ===================================================
def getAllBook():
    data = load_data()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()


    return books


# ========================================================
def getSingleBook(book_id: int ):
    data = load_data()

   
    query = "SELECT * FROM books WHERE book_id = %s"

    cursor.execute(query,(book_id,))

    book = cursor.fetchone()

    
    if book is None:
         raise HTTPException(
              status_code=404,
              detail="book not found"
         )
    
    return book




    # for book in data:
    #     if book["book_id"] == book_id:
    #         return book

    # raise HTTPException(
    #     status_code=404,
    #     detail="Book not found"
    # )





# =====================================================

def createNewBook(book : Book):
    data = load_data()

    try:
            query = """
            INSERT INTO books
            VALUES(%s,%s,%s,%s,%s,%s)
            """
    
            values = (
            book.book_id,
            book.title,
            book.author,
            book.genre,
            book.pages,
            book.rating
            )

            cursor.execute(query,values)
            connection.commit()
    except mysql.connector.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Book ID already exists"
        )
    
    


    


    # for b in data:
    #     if b["book_id"] == book.book_id:
    #         raise HTTPException(status_code=409,detail="User already exists",)
    
    

    # data.append(book.model_dump())
    # save_data(data)





# =======================================================

def sort_book(sort_by: str,order:str):
    valid_fields = ['pages','rating']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail='Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Invalid order select from between asc and desc")
    
    data = load_data()

    sorted_books = sorted(data,key=lambda book:book[sort_by],reverse=(order == 'desc'))
    return sorted_books


# =================  Update ==================
def updateBook(book_id: int, book: UpdateBook):
    try:
        query = """
            UPDATE books
            SET 
                title=%s,
                author=%s,
                genre=%s,
                pages=%s,
                rating=%s
            WHERE book_id = %s
        """
        values = (
            book.title,
            book.author,
            book.genre,
            book.pages,
            book.rating,
            book_id
        )

        cursor.execute(query, values)
        connection.commit()

       

    except mysql.connector.IntegrityError:
        raise HTTPException(status_code=400, detail="Integrity error while updating book")