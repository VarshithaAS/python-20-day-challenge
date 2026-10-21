# Day 15: Exception Handling in Python


# ==============================
# Question 1: Handle division by zero
# ==============================

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")


# ==============================
# Question 2: Handle invalid integer input
# ==============================

try:
    num = int("hello")
    print(num)
except ValueError:
    print("Invalid integer value")


# ==============================
# Question 3: Handle multiple exceptions
# ==============================

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")


# ==============================
# Question 4: Use try and finally
# ==============================

try:
    num = 10 / 2
    print(num)
finally:
    print("Program completed")


# ==============================
# Question 5: Use try and else
# ==============================

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("Your number is:", num)


# ==============================
# Question 6: Handle list index error
# ==============================

try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("List index is out of range")


# ==============================
# Question 7: Handle a missing dictionary key
# ==============================

try:
    student = {"name": "Varshitha", "age": 20}
    print(student["marks"])
except KeyError:
    print("Key not found")


# ==============================
# Question 8: Handle file not found
# ==============================

try:
    file = open("sample.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")


# ==============================
# Question 9: Use a general exception
# ==============================

try:
    num = int(input("Enter a number: "))
    print(100 / num)
except Exception as e:
    print("An error occurred:", e)


# ==============================
# Question 10: Handle an exception using raise
# ==============================

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Your age is:", age)

except ValueError as e:
    print("Error:", e)

# ==============================