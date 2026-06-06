import os

# Rename a file
os.rename("old_name.txt", "new_name.txt")

# Delete a file
os.remove("new_name.txt")

# Check if a file exists before opening
if os.path.exists("data.txt"):
    print("File exists and is ready to open.")
