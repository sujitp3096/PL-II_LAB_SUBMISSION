# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")
    file.write("This is the second line.\n")
print("File written successfully.\n")

# Reading from the fil
print("Reading from the file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to the file
with open("sample.txt", "a") as file:
    file.write("This line is appended at the end.\n")
print("Line appended to the file.\n")

# Reading again after appending
print("Reading the updated file:")
with open("sample.txt", "r") as file:
    print(file.read())
