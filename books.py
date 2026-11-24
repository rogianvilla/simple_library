import json
from pathlib import Path
from tabulate import tabulate

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

    def get_book(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                return book
        return None

    #Método para listar todos os livros cadastrados.
    def list_books(self):
        print("\n--- Lista de Livros ---")
        if not self.books:
            print("Nenhum livro cadastrado.")
            return
        else:
            print_data = []

            for book in self.books:
                print_data.append([book['id'], book['title'], book['author'], book['year'], book['amount'], book['amount_available']])
            
            print(tabulate(print_data, headers=["ID", "Título", "Autor", "Ano", "Quantidade", "Disponível"], tablefmt="grid"))

    #Método para listar livros por autor.
    def list_books_by_author(self, author):
        print(f"\n--- Livros de {author} ---")
        filtered_books = [book for book in self.books if book['author'].lower() == author.lower()]
        if not filtered_books:
            print(f"Nenhum livro encontrado para o autor {author}.")
            return
        else:
            for book in filtered_books:
                print(f"ID: {book['id']}, Título: {book['title']}, Autor: {book['author']}, Ano: {book['year']}, Quantidade: {book['amount']}, Disponível: {book['amount_available']}")

    #Método para listar livros por ano de publicação.
    def list_books_by_year(self, year):
        print(f"\n--- Livros do ano {year} ---")
        filtered_books = [book for book in self.books if book['year'] == year]
        if not filtered_books:
            print(f"Nenhum livro encontrado para o ano {year}.")
            return
        else:
            for book in filtered_books:
                print(f"ID: {book['id']}, Título: {book['title']}, Autor: {book['author']}, Ano: {book['year']}, Quantidade: {book['amount']}, Disponível: {book['amount_available']}")

    #Método para listar livros por título.
    def list_books_by_title(self, title):
        print(f"\n--- Livros com título'{title}' ---")
        filtered_books = [book for book in self.books if title.lower() in book['title'].lower()]
        if not filtered_books:
            print(f"Nenhum livro encontrado com o título '{title}'.")
            return
        else:
            for book in filtered_books:
                print(f"ID: {book['id']}, Título: {book['title']}, Autor: {book['author']}, Ano: {book['year']}, Quantidade: {book['amount']}, Disponível: {book['amount_available']}")

    def update_book(self, book_id, new_title, new_author, new_year, new_amount, new_amount_available):
        for book in self.books:
            if book['id'] == book_id:
                book['title'] = new_title
                book['author'] = new_author
                book['year'] = new_year
                book['amount'] = new_amount
                book['amount_available'] = new_amount_available
                print(f"Livro com ID {book_id} atualizado com sucesso.")
                return
        print(f"Nenhum livro encontrado com o ID {book_id}.")

    def remove_book(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                print(f"Livro com ID {book_id} removido com sucesso.")
                return
        print(f"Nenhum livro encontrado com o ID {book_id}.")