# 2. Python Data Structure Challenges in Real-World Scenarios
# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list.
# Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

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