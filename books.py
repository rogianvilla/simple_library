import itertools

class Books:
    _id_generator = itertools.count(start=1)
    
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year, amount, amount_available):
        book = {
            'title': title, 
            'author': author,
            'year': year,
            'amount': amount,
            'amount_available': amount_available,
            'id': next(self._id_generator)
        }
        self.books.append(book)

    