import json
from pathlib import Path
from datetime import date, datetime, timedelta
from users import Users
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

    def list_all_active_loans(self):
        if not self.loans:
            print("Nenhum empréstimo registrado.")
            return
        else:
            print_data = []

            for loan in self.loans:
                if not loan['returned']:
                    print_data.append([loan['loan_id'], loan['book_id'], loan['cpf'], loan['loan_date'], loan['expected_retur_date'], loan['return_date']])

            print(tabulate(print_data, headers=["ID Emprést.", "ID Livro", "CPF", "D.Empréstimo", "D. Prevista", "D. Devolução"], tablefmt="grid"))

    def list_all_loans(self):
        if not self.loans:
            print("Nenhum empréstimo registrado.")
            return
        else:
            print_data = []

            for loan in self.loans:
                print_data.append([loan['loan_id'], loan['book_id'], loan['cpf'], loan['loan_date'], loan['expected_retur_date'], loan['return_date']])

            print(tabulate(print_data, headers=["ID Emprést.", "ID Livro", "CPF", "D.Empréstimo", "D. Prevista", "D. Devolução"], tablefmt="grid"))

    def get_loans_by_user(self, cpf):
        user_loans = [loan for loan in self.loans if loan['cpf'] == cpf]
        if not user_loans:
            print(f"Nenhum empréstimo encontrado para o usuário com CPF {cpf}.")
            return
        else:
            for loan in user_loans:
                print(f"ID do Empréstimo: {loan['loan_id']}, ID do Livro: {loan['book_id']}, Data do Empréstimo: {loan['loan_date']}, Data de Devolução Esperada: {loan['expected_retur_date']}, Data de Devolução: {loan['return_date']}, Devolvido: {loan['returned']}")

    def get_loans_by_book(self, book_id):
        book_loans = [loan for loan in self.loans if loan['book_id'] == book_id]
        if not book_loans:
            print(f"Nenhum empréstimo encontrado para o livro com ID {book_id}.")
            return
        else:
            for loan in book_loans:
                print(f"ID do Empréstimo: {loan['loan_id']}, CPF do Usuário: {loan['cpf']}, Data do Empréstimo: {loan['loan_date']}, Data de Devolução Esperada: {loan['expected_retur_date']}, Data de Devolução: {loan['return_date']}, Devolvido: {loan['returned']}")

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