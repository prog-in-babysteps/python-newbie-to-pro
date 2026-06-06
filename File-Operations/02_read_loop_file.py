# Reading a file line by line in loop
with open('data\\books.txt', 'r') as book_file:
    for book_rec in book_file:
        print(book_rec.strip())
