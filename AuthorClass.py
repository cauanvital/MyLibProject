from DB_Connector import *


class Author:
    def __init__(self, authorname, shortbiography, birthyear, writinggenre, nationality):
        self.authorname = authorname
        self.shortbiography = shortbiography
        self.birthyear = birthyear
        self.writinggenre = writinggenre
        self.nationality = nationality

    def add_author_func(self):
        sql = "INSERT INTO Author(AuthorName, ShortBiography, BirthYear, WritingGenre, Nationality)" \
              "VALUES (?, ?, ?, ?, ?)"
        val = [
            self.authorname,
            self.shortbiography,
            self.birthyear,
            self.writinggenre,
            self.nationality
        ]

        mylibcursor.execute(sql, val)
        mylibdb.commit()
