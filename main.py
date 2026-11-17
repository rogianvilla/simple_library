from datetime import date, timedelta

from users import Users
from books import Books
from loans import Loans

users = Users()
books = Books()
loans = Loans()

def menu_livros():
    while True:
        print("\n--- Livros ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("0. Voltar")
        option = input("Escolha uma opção: ").strip()

        #Lẽ os inputs do usuário para cadastrar um livro
        if option == "1":
            title = input("Título do livro: ").strip()
            author = input("Autor do livro: ").strip()
            year = int(input("Ano de publicação: "))
            amount = int(input("Quantidade de cópias: "))
            amount_available = int(input("Quantidade disponível: "))

            books.add_book(title, author, year, amount, amount_available)
        elif option == "2":
            books.list_books()
        elif option == "0":
            return
        else:
            print("Opção inválida.")


def menu_usuarios():
    while True:
        print("\n--- Usuários ---")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("0. Voltar")
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            pass
        elif option == "2":
            pass
        elif option == "0":
            return
        else:
            print("Opção inválida.")


def menu_emprestimos():
    while True:
        print("\n--- Empréstimos ---")
        print("1. Registrar empréstimo")
        print("2. Registrar devolução")
        print("3. Listar empréstimos ativos")
        print("0. Voltar")
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            pass
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "0":
            return
        else:
            print("Opção inválida.")


def menu_relatorios():
    while True:
        print("\n--- Relatórios ---")
        print("1. Resumo da biblioteca")
        print("2. Empréstimos ativos")
        print("0. Voltar")
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            pass
        elif option == "2":
            pass
        elif option == "0":
            return
        else:
            print("Opção inválida.")


def main():
    while True:
        print("\n=== Sistema da Biblioteca ===")
        print("1. Livros")
        print("2. Usuários")
        print("3. Empréstimos")
        print("4. Relatórios")
        print("0. Sair")
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            menu_livros()
        elif option == "2":
            menu_usuarios()
        elif option == "3":
            menu_emprestimos()
        elif option == "4":
            menu_relatorios()
        elif option == "0":
            books.save_books()
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()