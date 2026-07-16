import mysql.connector

connection =mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)


print(connection)

db_name = "library_db"

mycursor = connection.cursor()

sqlquery = "CREATE DATABASE " + db_name

mycursor.execute(sqlquery)

