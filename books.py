class Books:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = {'title': title, 'author': author}
        self.books.append(book)

    def get_books(self):
        return self.books