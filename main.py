#create a book class and initialise objects and attributes
class Library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print('Books in the library.')
        for book in self.books:
            print(book)

    def add_book(self, book):
        print("Book added to the library.")
        self.books.insert(o,add_book)

    def borrow_book(self, borrow_book):
        for borrow_book in self.books:
            print("You have borrowed a book")
            self.books.remove(borrow_book)

    def receive_book(self, receive_book):
        print("You have returned a book")
        self.books.append(receive_book)

    def delete_book(self, delete_book):
        print("Book name is deleted")
        self.books.remove(delete_book)


books = ['Jane Eyre, Recipe for disaster, My children have faces, Things fall apart']
o = Library(books)




    #create an instance of list of books
#book1 = Book("Jane Eyre", "Charlotte Bronte")
#book2 = Book("Recipe for disaster", "Lilian Tindyebwa")
#book3 = Book("My children have faces", "Carol Campbell")
#book4 = Book("Things fall apart", "Chinua Achebe")


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
    choice = int(input("Enter your choice: "))
    if choice == 1:
        o.list_books()
    elif choice == 2:
        book = input("Enter Book Name:")
        o.add_book(book)

    elif choice == 3:
        book = input("Enter the Book Name to Borrow: ")
        o.borrow_book(book)

    elif choice == 4:
        book = input("Enter book returned: ")
        o.receive_book(book)

    elif choice == 5:
        book = input("Enter Deleted Book: ")
        o.delete_book(book)



