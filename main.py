from Table_Creator import *

tables_generator()

from AddBook import *
from AddAuthor import *

i = None

while i != 0:
    print("1 para adicionar livro, 2 para adicionar autor, 0 para fechar o programa.")
    i = int(input("Insira sua escolha: "))

    while i != 1 and i != 2 and i != 0:
        print("Opção Inválida!")
        i = int(input("Insira sua escolha: "))

    if i == 1:
        newbook = Book(
                input("Book name: "),
                input("Author name: "),
                input("Short sinopse: "),
                input("Publishing company: "),
                input("Publication year: "),
                input("Book genre: "),
                input("Book volume: "),
                input("Rate the book between 1 and 5: ")
        )
        newbook.add_book_func()
    elif i == 2:
        newauthor = Author(
            input("Author name: "),
            input("Short biography: "),
            input("Author birth year: "),
            input("Writing genre: "),
            input("Author nationality: ")
        )
        newauthor.add_author_func()
    else:
        print("Tenha um bom dia")
        break
