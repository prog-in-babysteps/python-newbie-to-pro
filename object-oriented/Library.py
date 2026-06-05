from Book import Book
class Library:

    def __init__(self, name):
        self.name = name
        self._catalog = {}

    def add_book(self, book):
        """Adds a new Book instance to the internal catalog dictionary."""
        if book.isbn in self._catalog:
            print(f"Error: Book with ISBN {book.isbn} already exists.")
        else:
            self._catalog[book.isbn] = book
            print(f"Success: Added '{book.title}' to the catalog.")

    def display_inventory(self):
        """Iterates through and prints all stored Book instances."""
        print(f"\n--- {self.name} Catalog ---")
        if not self._catalog:
            print("The library is currently empty.")
            return
        for book in self._catalog.values():
            book.display_book()

    def borrow_book(self, isbn):
        """Finds a book by ISBN and triggers its checkout logic."""
        book = self._catalog.get(isbn)
        if not book:
            print("Error: Book not found in catalog.")
        elif book.checkout_book():
            print(f"Success: You borrowed '{book.title}'.")
        else:
            print(f"Error: '{book.title}' is already checked out.")

    def return_book(self, isbn):
        """Finds a book by ISBN and triggers its return logic."""
        book = self._catalog.get(isbn)
        if not book:
            print("Error: This book does not belong to this library.")
        elif book.return_book():
            print(f"Success: '{book.title}' has been returned.")
        else:
            print(f"Error: '{book.title}' was not checked out.")
