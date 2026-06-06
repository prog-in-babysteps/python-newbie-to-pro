# Reading a file line by line in loop
authors_list = set()
with open('data\\books.txt', 'r') as book_file:
    for book_rec in book_file:
        book_rec = book_rec.strip()
        name, isbn, price, author, num_pages = book_rec.split(",")
        print(f"Book Author: {author}")
        # Add Author to set
        authors_list.add(author)

with open('data\\authors.txt', 'w') as authors_file:
    for author in authors_list:
        authors_file.write(f"Author Name: {author}\n")
