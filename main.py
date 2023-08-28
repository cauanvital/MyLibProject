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
        add_book_func()
    elif i == 2:
        add_author_func()
    else:
        print("Tenha um bom dia")
        break
