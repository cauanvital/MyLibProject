import mysql.connector


def database_creator():
    creatorconnector = mysql.connector.connect(
        # Placeholder host
        host="localhost",
        # Placeholder user
        user="Joca",
        # Placeholder password
        password="6r72Jo^#HBU6"
    )

    creatorconnectorcursor = creatorconnector.cursor()

    creatorconnectorcursor.execute("CREATE DATABASE IF NOT EXISTS mylibdatabase")


def tables_generator():
    mylibdb = mysql.connector.connect(
        host="localhost",
        user="Joca",
        password="6r72Jo^#HBU6",
        database="mylibdatabase"
    )

    mylibcursor = mylibdb.cursor()

    mylibcursor.execute("CREATE TABLE IF NOT EXISTS Book("
                        "BookId INT AUTO_INCREMENT PRIMARY KEY,"
                        "BookName VARCHAR (255),"
                        "AuthorName VARCHAR (255),"
                        "ShortSinopse VARCHAR (255),"
                        "PublishingCompany VARCHAR (255),"
                        "PublicationYear YEAR,"
                        "Genre VARCHAR (255),"
                        "Volume VARCHAR (6),"
                        "Rating INT (1))")

    mylibcursor.execute("CREATE TABLE IF NOT EXISTS Author("
                        "AuthorId INT AUTO_INCREMENT PRIMARY KEY,"
                        "AuthorName VARCHAR (255),"
                        "ShortBiography VARCHAR (255),"
                        "BirthYear YEAR,"
                        "WritingGenre VARCHAR (255),"
                        "Nationality VARCHAR (255))")
