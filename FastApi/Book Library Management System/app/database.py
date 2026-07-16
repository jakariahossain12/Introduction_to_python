import json

import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "library_db"
)

cursor = connection.cursor(dictionary=True)


def load_data():
    with open("books.json","r") as f :
        data = json.load(f)
        return data
    

def save_data(data):
    with open("books.json","w") as f:
        json.dump(data,f)

def fetchAllBook():
    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()
    print(books)

