from indices import Indices
from users import Users
from books import Books
from loans import Loans

users = Users()
books = Books()
loans = Loans()
indices = Indices()

def menu_livros():
    while True:
        print("\n--- Livros ---")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Remover livro")
        print("0. Voltar")
        option = input("Escolha uma opção: ").strip()

        #Lê os inputs do usuário para cadastrar um livro
        if option == "1":
            title = input("Título do livro: ").strip()
            author = input("Autor do livro: ").strip()
            year = int(input("Ano de publicação: "))
            amount = int(input("Quantidade de cópias: "))
            amount_available = int(input("Quantidade disponível: "))
            book_id = indices.get_indices()['books']['last_id'] + 1

            books.add_book(title, author, year, amount, amount_available, book_id)

            #Atualiza o último ID de livro no arquivo de índices
            indices.get_indices()['books']['last_id'] = book_id
        elif option == "2":
            #Método para listar livros cadastrados, por autor, por título ou por ano de publicação
            while True:
                print("\n--- Listar Livros para atualizar ---")
                print("1. Listar livros por autor")
                print("2. Listar livros por titulo")
                print("3. Listar livros por ano de publicação")
                print("0. Voltar")
                list_option = input("Escolha uma opção: ").strip()
                        
                if list_option == "1":
                    books.list_books_by_author(input("Digite o nome do autor: ").strip())
                elif list_option == "2":
                    books.list_books_by_title(input("Digite o título do livro: ").strip())
                elif list_option == "3":
                    books.list_books_by_year(int(input("Digite o ano de publicação: ")))
                elif list_option == "0":
                    break
                else:
                    print("Opção inválida.")    
        elif option == "3":
            #Método para atualizar livros cadastrados
            print("\n--- Listar Livros para atualizar ---")
            while True:
                print("1. Listar livros por autor")
                print("2. Listar livros por titulo")
                print("3. Listar livros por ano de publicação")
                print("0. Voltar")
                list_option = input("Escolha uma opção: ").strip()
                    
                if list_option == "1":
                    books.list_books_by_author(input("Digite o nome do autor: ").strip())
                    break
                elif list_option == "2":
                    books.list_books_by_title(input("Digite o título do livro: ").strip())
                    break
                elif list_option == "3":
                    books.list_books_by_year(int(input("Digite o ano de publicação: ")))
                    break
                else:
                    print("Opção inválida.")

            book_id = int(input("\nDigite o ID do livro que deseja atualizar: "))
            book = books.get_book(book_id)
            print("\nDigite os novos dados do livro (deixe em branco para manter o valor atual):")
            new_title = input("Novo título do livro: ").strip() if input("Novo título do livro: ").strip() != "" else book['title']
            new_author = input("Novo autor do livro: ").strip() if input("Novo autor do livro: ").strip() != "" else book['author']
            new_year = int(input("Novo ano de publicação: ")) if input("Novo ano de publicação: ").strip() != "" else book['year']
            new_input = input("Nova quantidade de cópias: ").strip()
            new_amount = int(new_input) if new_input != "" else book['amount']
            new_amount_available = book['amount_available'] + (new_amount - book['amount']) if book else 0
            books.update_book(book_id, new_title, new_author, new_year, new_amount, new_amount_available)

        elif option == "4":
            #Método para deletar livros cadastrados
            print("\n--- Listar Livros para deletar ---")
            while True:
                print("1. Listar livros por autor")
                print("2. Listar livros por titulo")
                print("3. Listar livros por ano de publicação")
                print("0. Voltar")
                list_option = input("Escolha uma opção: ").strip()
                        
                if list_option == "1":
                    books.list_books_by_author(input("Digite o nome do autor: ").strip())
                    break
                elif list_option == "2":
                    books.list_books_by_title(input("Digite o título do livro: ").strip())
                    break
                elif list_option == "3":
                    books.list_books_by_year(int(input("Digite o ano de publicação: ")))
                    break
                else:
                    print("Opção inválida.")

            book_id = int(input("\nDigite o ID do livro que deseja deletar: "))

            book = books.remove_book(book_id)

        elif option == "0":
            return
        else:
            print("Opção inválida.")

#Menu usuários com opções para cadastrar, listar atualizar e excluir usuários
def menu_usuarios():
    while True:
        print("\n--- Usuários ---")
        print("1. Cadastrar usuário")
        print("2. Consultar usuários")
        print("3. Atualizar usuários")
        print("4. Excluir usuário")
        print("0. Voltar")
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            name = input("Nome do usuário: ").strip()
            email = input("Email do usuário: ").strip()
            cpf = input("CPF do usuário: ").strip()
            cpf = ''.join(filter(str.isdigit, cpf))

            if users.verify_user(cpf):
                print(f"Usuário com CPF {cpf} já está cadastrado.")
            else:
                if Users.cpf_validate(cpf):
                    users.add_user(name, email, cpf)
                    print(f"Usuário {name} cadastrado com sucesso.")
                else:
                    print(f"CPF {cpf} inválido.")

        elif option == "2":
            print("\n--- Consultar Usuário ---")
            cpf = input("Digite o CPF do usuário que deseja consultar: ").strip()
            cpf = ''.join(filter(str.isdigit, cpf))
            user = users.get_user(cpf)
            if user:
                print(f"Nome: {user['name']}, Email: {user['email']}, CPF: {user['cpf']}")
            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
        elif option == "3":
            print("\n--- Atualizar Usuário ---")
            cpf = input("Digite o CPF do usuário que deseja atualizar: ").strip()
            cpf = ''.join(filter(str.isdigit, cpf))
            user = users.get_user(cpf)
            print("\nDigite os novos dados do usuário (deixe em branco para manter o valor atual):")
            if user:
                new_input_name = input("Novo nome: ").strip()
                new_name = new_input_name if new_input_name != "" else user['name']
                new_input_email = input("Novo email: ").strip()
                new_email = new_input_email if new_input_email != "" else user['email']
                users.update_user(cpf, new_name, new_email)
            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
        elif option == "4":
            print("\n--- Excluir Usuário ---")
            cpf = input("Digite o CPF do usuário que deseja excluir: ").strip()
            cpf = ''.join(filter(str.isdigit, cpf))

            if users.verify_user(cpf):
                confirm = input(f"Tem certeza que deseja excluir o usuário com CPF {cpf}? (s/n): ").strip().lower()
                if confirm == "s":
                    users.remove_user(cpf)
                else:
                    print("Exclusão cancelada.")
            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
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
        print("1. Listas todos os livros cadastrados")
        print("2. Lista todos os usuários cadastrados")
        print("3. Lista todos os empréstimos ativos")
        print("0. Voltar")
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            books.list_books()
        elif option == "2":
            users.list_all_users()
        elif option == "3":
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
            indices.save_indices()
            users.save_users()
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()