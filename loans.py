import json
from users import Users
from books import Books
from pathlib import Path
from datetime import date, datetime, timedelta
from tabulate import tabulate

class Loans:
    def __init__(self):
        if Path("Collections/loans.json").exists():
            with open("Collections/loans.json", "r") as file:
                self.loans = json.load(file)
        else:
            self.loans = []

    def save_loans(self):
        with open("Collections/loans.json", "w", encoding="utf-8") as new_file:
            json.dump(self.loans, new_file, ensure_ascii=False, indent=4)

    def add_loan(self, book_id, cpf, return_date, returned, loan_id):
        loan_date = datetime.strptime(date.today().strftime("%d/%m/%Y"), "%d/%m/%Y")
        expected_loan_date = (loan_date + timedelta(days=7)).strftime("%d/%m/%Y")

        loan = {
            'book_id': book_id,
            'cpf': cpf,
            'loan_date': loan_date.strftime("%d/%m/%Y"),
            'expected_retur_date': expected_loan_date,
            'return_date': return_date,
            'returned': returned,
            'loan_id': loan_id
        }
        self.loans.append(loan)

    def list_all_active_loans(self, books, users):
        if not self.loans:
            print("Nenhum empréstimo registrado.")
            return
        else:
            print_data = []

            for loan in self.loans:
                if not loan['returned']:
                    print_data.append([loan['loan_id'], loan['book_id'], books.get_book(loan['book_id'])['title'], loan['cpf'], users.get_user(loan['cpf'])['name'], loan['loan_date'], loan['expected_retur_date'], loan['return_date']])

            print(tabulate(print_data, headers=["ID Emprést.", "ID Livro", "Título", "CPF", "Nome", "D.Empréstimo", "D. Prevista", "D. Devolução"], tablefmt="grid"))

    def list_all_loans(self, books, users):
        if not self.loans:
            print("Nenhum empréstimo registrado.")
            return
        else:
            print_data = []

            for loan in self.loans:
                print_data.append([loan['loan_id'], loan['book_id'], books.get_book(loan['book_id'])['title'], loan['cpf'], users.get_user(loan['cpf'])['name'], loan['loan_date'], loan['expected_retur_date'], loan['return_date']])

            print(tabulate(print_data, headers=["ID Emprést.", "ID Livro", "Título", "CPF", "Nome", "D.Empréstimo", "D. Prevista", "D. Devolução"], tablefmt="grid"))

    def get_loans_by_user(self, user, books):
        if not user:
            print(f"Nenhum empréstimo encontrado para o usuário com CPF {user['cpf']}.")
            return
        else:
            print_data = []
            for loan in self.loans:
                print_data.append([loan['loan_id'], loan['book_id'], books.get_book(loan['book_id'])['title'], loan['cpf'], user['name'], loan['loan_date'], loan['expected_retur_date'], loan['return_date'], loan['returned']])
            
            print(tabulate(print_data, headers=["ID Emprést.", "ID Livro" , "Titulo", "CPF", "Nome", "D.Empréstimo", "D. Prevista", "D. Devolução", "Devolvido"], tablefmt="grid"))

    def get_loans_by_book(self, book, users):
        if not book:
            print(f"Nenhum empréstimo encontrado para o livro com ID {book['id']}.")
            return
        else:
            print_data = []
            for loan in self.loans:
                print_data.append([loan['loan_id'], loan['book_id'], book['title'], loan['cpf'], users.get_user(loan['cpf'])['name'], loan['loan_date'], loan['expected_retur_date'], loan['return_date'], loan['returned']])
            
            print(tabulate(print_data, headers=["ID Emprést.", "ID Livro", "CPF", "D.Empréstimo", "D. Prevista", "D. Devolução", "Devolvido"], tablefmt="grid"))

    def update_loan(self, book_id, cpf):
        for loan in self.loans:
            if loan['book_id'] == book_id and loan['cpf'] == cpf:
                loan['returned'] = True
                loan['return_date'] = datetime.now().strftime("%d/%m/%Y")
                return True
        return False

    def get_active_loan(self, cpf, book_id):
        for loan in self.loans:
            if loan['cpf'] == cpf and loan['book_id'] == book_id and loan['returned'] == False:
                return True
        return False