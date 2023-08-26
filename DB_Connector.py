import mysql.connector

mylibdb = mysql.connector.connect(
    host="localhost",
    user="Joca",
    password="6r72Jo^#HBU6",
    database="mylibdatabase"
)

mylibcursor = mylibdb.cursor()