from Book import *
from Library import *

# Instantiate Library object
my_library = Library("Chennai City Library")

# Instantiate Book objects
book1 = Book("100", "Ponniyin Selvan", "Kalki", 500)
book2 = Book("200", "En Iniya Iyanthira", "Sujatha", 200)
book3 = Book("300", "Thirukural", "Thiruvalluvar", 150)

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# View initial catalog status
my_library.display_inventory()

# Borrow a book
my_library.borrow_book("100")

# View initial catalog status - After borrow
my_library.display_inventory()

# Try borrowing the same book again
my_library.borrow_book("100")

# Return the book back to inventory
my_library.return_book("100")

# View initial catalog status - After return
my_library.display_inventory()
