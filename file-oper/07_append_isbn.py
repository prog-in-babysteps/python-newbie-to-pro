# Reading a file line by line in loop
book_isbn = {}
with open('data\\new_books.txt', 'r') as book_file:
    for book_rec in book_file:
        book_rec = book_rec.strip()
        name, isbn, price, author, num_pages = book_rec.split(",")
        print(f"Book Name: {name} ISBN: {isbn}")
        book_isbn[name] = isbn


# Append to an existing file
with open('data\\isbn.txt', 'a') as isbn_file:
    for name, isbn in book_isbn.items():
        isbn_file.write(f"Book Name: {name} ISBN: {isbn}\n")
