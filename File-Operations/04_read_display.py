# Reading a file line by line in loop
with open('data\\books.txt', 'r') as book_file:
    for book_rec in book_file:
        book_rec = book_rec.strip()
        name, isbn, price, author, num_pages = book_rec.split(",")
        print(f"Book Name: {name}")
        print(f"Book Author: {author}")
        print(f"Book Price: ${price}")

