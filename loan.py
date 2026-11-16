class Loan:
    def __init__(self, book, user, due_date):
        self.book = book
        self.user = user
        self.due_date = due_date
        self.active = True

    def return_book(self):
        self.active = False