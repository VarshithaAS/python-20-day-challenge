
# Day 14: File Handling in Python


# ==============================
# Question 1: Create a file and write content
# ==============================

with open("sample.txt", "w") as file:
    file.write("Welcome to Python")


# ==============================
# Question 2: Read content from a file
# ==============================

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# ==============================
# Question 3: Write multiple lines
# ==============================

with open("sample.txt", "w") as file:
    file.write("Python\n")
    file.write("Programming\n")
    file.write("Practice")


# ==============================
# Question 4: Read all content
# ==============================

with open("sample.txt", "r") as file:
    print(file.read())


# ==============================
# Question 5: Append content to a file
# ==============================

with open("sample.txt", "a") as file:
    file.write("\nFile Handling")


# ==============================
# Question 6: Read the first line
# ==============================

with open("sample.txt", "r") as file:
    print(file.readline())


# ==============================
# Question 7: Read all lines into a list
# ==============================

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)


# ==============================
# Question 8: Count the number of lines
# ==============================

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))


# ==============================
# Question 9: Write your name into a file
# ==============================

name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)


# ==============================
# Question 10: Read a file and count characters
# ==============================

with open("sample.txt", "r") as file:
    content = file.read()
    print("Number of characters:", len(content))
