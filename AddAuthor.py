from DB_Connector import *


def add_author_func():
    bookclass = {
        "AuthorName": input("Author name: "),
        "ShortBiography": input("Short biography: "),
        "BirthYear": input("Author birth year: "),
        "WritingGenre": input("Writing genre: "),
        "Nationality": input("Author nationality: ")
    }

    sql = "INSERT INTO Author(AuthorName, ShortBiography, BirthYear, WritingGenre, Nationality)" \
          "VALUES (%s, %s, %s, %s, %s)"
    val = list(bookclass.values())

    mylibcursor.execute(sql, val)

    mylibdb.commit()
