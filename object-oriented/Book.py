class Book:

    def __init__(self, isbn, title, author, numpages):
        # Properties
        self.isbn = isbn
        self.title = title
        self.author = author
        self.numpages = numpages
        self._is_borrowed = False

    def checkout_book(self):
        """Marks the book as borrowed if it is available."""
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned if it was checked out."""
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False

    def display_book(self):
        """String representation when printed."""
        status = "Borrowed" if self._is_borrowed else "Available"
        print(f"'[{self.isbn}] {self.title}' by {self.author} Num Pages: {self.numpages} Status: [{status}]")
