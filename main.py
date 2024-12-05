#create a book class and initialise objects and attributes

class Library:
    def __init__(self, books):
        # Use a dictionary where the book name is the key, and the value stores book details
        self.books = books

    def list_books(self):
        if not self.books:
            print("\nThe library has no books currently.")
        else:
            print("\nBooks in the library:")
            for book, details in self.books.items():
                status = "Available" if details["available"] else "Borrowed"
                print(f"- {book} ({status})")

    def add_book(self, book, author):
        if book in self.books:
            print(f"The book '{book}' is already in the library.")
        else:
            self.books[book] = {"author": author, "available": True}
            print(f"The book '{book}' by {author} has been added to the library.")

    def borrow_book(self, book):
        if book not in self.books:
            print(f"The book '{book}' is not available in the library.")
        elif not self.books[book]["available"]:
            print(f"The book '{book}' is currently borrowed.")
        else:
            self.books[book]["available"] = False
            print(f"You have borrowed the book '{book}'. Enjoy reading!")

    def return_book(self, book):
        if book not in self.books:
            print(f"The book '{book}' does not belong to our library.")
        elif self.books[book]["available"]:
            print(f"The book '{book}' is already in the library.")
        else:
            self.books[book]["available"] = True
            print(f"Thank you for returning the book '{book}'.")

    def delete_book(self, book):
        if book in self.books:
            del self.books[book]
            print(f"The book '{book}' has been removed from the library.")
        else:
            print(f"The book '{book}' is not in the library.")


# Initialize the library with some books
books = {
    "Jane Eyre": {"author": "Charlotte Bronte", "available": True},
    "Recipe for Disaster": {"author": "Lilian Tindyebwa", "available": True},
    "My Children Have Faces": {"author": "Carol Campbell", "available": True},
    "Things Fall Apart": {"author": "Chinua Achebe", "available": True},
    "I Will Marry When I Want": {"author": "Ngugi wa Thiong'o", "available": True},
    "No Longer at Ease": {"author": "Chinua Achebe", "available": True},
}
library = Library(books)

# Menu for the library system
msg = """
Library Management System
1. Display Books
2. Add Book
3. Borrow Book
4. Return Book
5. Delete Book
6. Exit
"""

# Menu-driven program loop
while True:
    print(msg)
    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        library.list_books()
    elif choice == 2:
        book = input("Enter the Book Name: ").strip()
        author = input("Enter the Author's Name: ").strip()
        library.add_book(book, author)
    elif choice == 3:
        book = input("Enter the Book Name to Borrow: ").strip()
        library.borrow_book(book)
    elif choice == 4:
        book = input("Enter the Book Name to Return: ").strip()
        library.return_book(book)
    elif choice == 5:
        book = input("Enter the Book Name to Delete: ").strip()
        library.delete_book(book)
    elif choice == 6:
        print("Thank you for using the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")





