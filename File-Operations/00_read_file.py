# Open a file for reading
book_file = open('data\\books.txt', mode='r')

# Read from the file
data = book_file.read(62)
print("Data Read from the file:")
print(data)

# Close the file
book_file.close()
