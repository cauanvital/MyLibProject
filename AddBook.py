from DB_Connector import *


class Book:
    def __init__(self, bookname, authorname, shortsinopse, publishingcompany, publicationyear, genre, volume, rating):
        self.bookname = bookname
        self.authorname = authorname
        self.shortsinopse = shortsinopse
        self.publishingcompany = publishingcompany
        self.publicationyear = publicationyear
        self.genre = genre
        self.volume = volume
        self.rating = rating

    def add_book_func(self):
        sql = "INSERT INTO Book(BookName, AuthorName, ShortSinopse, PublishingCompany, PublicationYear, Genre, Volume, " \
              "Rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        val = [self.bookname,
               self.authorname,
               self.shortsinopse,
               self.publishingcompany,
               self.publicationyear,
               self.genre,
               self.volume,
               self.rating]

        mylibcursor.execute(sql, val)
        mylibdb.commit()
