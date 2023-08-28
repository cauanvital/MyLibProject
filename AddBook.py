from DB_Connector import *


def add_book_func():
    addbook = {
        "BookName": input("Book name: "),
        "AuthorName": input("Author name: "),
        "ShortSinopse": input("Short sinopse: "),
        "PublishingCompany": input("Publishing company: "),
        "PublicationYear": input("Publication year: "),
        "Genre": input("Book genre: "),
        "Volume": input("Book volume: "),
        "Rating": input("Rate the book between 1 and 5: ")
    }

    sql = "INSERT INTO Book(BookName, AuthorName, ShortSinopse, PublishingCompany, PublicationYear, Genre, Volume, " \
          "Rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    val = list(addbook.values())

    mylibcursor.execute(sql, val)

    mylibdb.commit()
