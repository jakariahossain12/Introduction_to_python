import mysql.connector

connection =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database = "library_db"
)






mycursor = connection.cursor()

sqlquery = """
            CREATE TABLE books (
            book_id INT PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
            genre VARCHAR(50),
            pages INT,
            rating FLOAT

            )
"""

mycursor.execute(sqlquery)

