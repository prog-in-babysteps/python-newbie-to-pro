# Reading a file line by line
with open('data\\books.txt', 'r') as book_file:
    line_1 = book_file.readline()
    line_2 = book_file.readline()
    print("Line-1: ", line_1)
    print("Line-2: ", line_2)
