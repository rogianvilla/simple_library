import itertools
import json
from pathlib import Path

class Books:
    #Construtor da classe Books, que carrega os livros do arquivo JSON se ele existir, ou inicializa uma lista vazia caso contrário.
    def __init__(self):
        if Path("Collections/books.json").exists():
            with open("Collections/books.json", "r") as file:
                self.books = json.load(file)
        else:
            self.books = []

    #Destrutor da classe Books, que salva os livros no arquivo JSON ao encerrar o programa.
    def save_books(self):
        with open("Collections/books.json", "w", encoding="utf-8") as new_file:
            json.dump(self.books, new_file, ensure_ascii=False, indent=4)


    #Método para adicionar um livro à coleção. Recebe os parâmetros do livro, cria um dicionário representando o livro e adiciona à lista de livros.
    def add_book(self, title, author, year, amount, amount_available, book_id):
        book = {
            'title': title, 
            'author': author,
            'year': year,
            'amount': amount,
            'amount_available': amount_available,
            'id': book_id
        }
        self.books.append(book)

    #Método para listar todos os livros cadastrados. Se não houver livros, exibe uma mensagem informando que nenhum livro foi cadastrado. Caso contrário, percorre a lista de livros e imprime as informações de cada livro.
    def list_books(self):
        if not self.books:
            print("Nenhum livro cadastrado.")
            return
        for book in self.books:
            print(f"ID: {book['id']}, Título: {book['title']}, Autor: {book['author']}, Ano: {book['year']}, Quantidade: {book['amount']}, Disponível: {book['amount_available']}")
    