import json
from pathlib import Path
from datetime import date, datetime, timedelta

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
