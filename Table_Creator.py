import pymongo


def tables_generator():
    mylibdb = sqlite3.connect("mylibdatabase.db")

    mylibcursor = mylibdb.cursor()

    mylibcursor.execute("CREATE TABLE IF NOT EXISTS Book("
                        "BookId INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "BookName VARCHAR (255),"
                        "AuthorName VARCHAR (255),"
                        "ShortSinopse VARCHAR (255),"
                        "PublishingCompany VARCHAR (255),"
                        "PublicationYear YEAR,"
                        "Genre VARCHAR (255),"
                        "Volume VARCHAR (6),"
                        "Rating INT (1))")

    mylibcursor.execute("CREATE TABLE IF NOT EXISTS Author("
                        "AuthorId INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "AuthorName VARCHAR (255),"
                        "ShortBiography VARCHAR (255),"
                        "BirthYear YEAR,"
                        "WritingGenre VARCHAR (255),"
                        "Nationality VARCHAR (255))")
