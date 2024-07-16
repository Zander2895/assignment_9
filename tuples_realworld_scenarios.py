class LibrarySystem:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        new_book = (title, author, isbn)

        if not any(book[2] == isbn for book in self.books):
            self.books.append(new_book)
            print(f"Book '{title}' added successfully.")
        else:
            print(f"Book with ISBN '{isbn}' already exists.")

    def display_books(self):
        for book in self.books:
            print(f"Title: {book[0]}, Author: {book[1]}, ISBN: {book[2]}")

library = LibrarySystem()
library.add_book("1984", "George Orwell", "04844881")
library.add_book("1984", "George Orwell", "04844881")
library.add_book("Brave New World", "Aldous Huxley", "04844662")
library.display_books()