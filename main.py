#create a book class and initialise objects and attributes
class Library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("\nBooks in the library: ")
        for book in self.books:
            print(f"- {book}")

    def add_book(self, book):
        if book in self.books:
            print(f"The book '{book}' is already in the library.")
        else:
            self.books.append(book)
            print(f"The book'{book}' is added to the library.")

    def borrow_book(self, borrow_book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed a book '{book}'.")
        else:
            print(f"The book '{book}' is not available.")

    def return_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print("Thank you for returning the book '{book}'.")
        else:
            print(f"The book '{book}' is already in the library")

    def delete_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"The book '{book}' has been deleted.")
        else:
            print(f"The book '{book}' is not our library.")


#library is initialised with books
books = ['Jane Eyre, Recipe for disaster, My children have faces, Things fall apart, I will marry when I want, No longer at ease']
library = Library(books)


msg = """
1. Display Books
2. Add Book
3. Borrow Book
4. Return Book
5. Delete Book
6. Exit
"""
while True:
    print(msg)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number between 1 and 6.")
        continue

    if choice == 1:
        library.list_books()
    elif choice == 2:
        book = input("Enter Book Name: ")
        library.add_book(book.strip())

    elif choice == 3:
        book = input("Enter the Book Name to Borrow: ")
        library.borrow_book(book.strip())

    elif choice == 4:
        book = input("Enter book returned: ")
        library.return_book(book.strip())

    elif choice == 5:
        book = input("Enter Deleted Book: ")
        library.delete_book(book.strip())
    elif choice == 6:
        print("Thank you for using our library. ")
        break
    else:
        print("Invalid choice! Enter a number between 1 and 6.")



