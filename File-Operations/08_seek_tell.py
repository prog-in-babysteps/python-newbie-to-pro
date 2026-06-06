import os

with open("data\\sample.txt", "r") as alphabet_file:
    print(alphabet_file.read(5))  # Reads first 5 characters
    print(alphabet_file.tell())   # Outputs: 5
    print(alphabet_file.read(5))  # Reads first 5 characters
    print(alphabet_file.tell())   # Outputs: 10
    alphabet_file.seek(20, os.SEEK_SET) # Move the File Pointer to 20th byte from Start
    print(alphabet_file.read(5))  # Reads first 5 characters
    print(alphabet_file.tell())   # Outputs: 5
