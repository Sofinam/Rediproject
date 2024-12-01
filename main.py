#create a book class and initialise objects and attributes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return (f"Title: {self.title}, "
                f"Author: {self.author}, "
                f"Borrowed: {'Yes' if self.is_borrowed else 'Not yet'}")

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email =email

    def __str__(self):
        return f"User ID> {self.user_id}, Name: {self.name}, Email: {self.email}"

class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book):...
    def list_books(self):...
    def borrow_book(self, title):...
    def return_book(self, title):...
    def add_user(self, user):
        if user.user_id in self.users:
            print(f"User ID {user.user_id} already exists")
            return
        self.users[user.user_id] = user
        print(f"User '{user.name}' added with ID {user.user_id}.")

    def list_users(self):
        if not self.users:
            print("No users registered")
            return
        for user_id, user in self.users.items():
            print(user)

    def update_user(self, user_id, name=None, email=None):
        if user_id not in self.users:
            print("User not found")
            return
        if name:
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
        print(f"User '{user_id}' updated.")

    #method takes in a book object as its parameter
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    #lists all books in the library
    def list_books(self):
        if not self.books:
            print('There are no books in the library.')
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.author}'.")
                return
        print('Book is not available. or has been borrowed')

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.author}'.")
                return
        print('Book is not available. or has not been borrowed')
#create an instance of list of books
book1 = Book("Jane Eyre", "Charlotte Bronte")
book2 = Book("Recipe for disaster", "Lilian Tindyebwa")
book3 = Book("My children have faces", "Carol Campbell")
book4 = Book("Things fall apart", "Chinua Achebe")

print(book1)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_book(Book("Small Worlds", "Caleb Azumah"))

print()

library.list_books()

print()

library.borrow_book("Things fall apart")
library.borrow_book("Jane Eyre")
library.borrow_book("I will marry when I want")

print()

library.return_book("Things fall apart")
library.return_book("Jane Eyre")

print()
library.add_user(User("001", "Mary Ann", "maryann@gmail.com"))
library.add_user(User("002", "Gill Smith", "gillsmith@gmail.com"))

print()

library.list_users()

print()

library.update_user("002", email="gsmith@gmail.com")


print()

library.list_users()

