# Day 08: Loops in Python

# ==============================
# Question 1: Print numbers from 1 to 10
# ==============================

for i in range(1, 11):
    print(i)


# ==============================
# Question 2: Print even numbers from 1 to 20
# ==============================

for i in range(2, 21, 2):
    print(i)


# ==============================
# Question 3: Print numbers from 10 to 1
# ==============================

for i in range(10, 0, -1):
    print(i)


# ==============================
# Question 4: Print the multiplication table of 5
# ==============================

for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


# ==============================
# Question 5: Find the sum of numbers from 1 to 10
# ==============================

total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)


# ==============================
# Question 6: Print each fruit in a list
# ==============================

fruits = ["Apple", "Mango", "Orange", "Grapes"]

for fruit in fruits:
    print(fruit)


# ==============================
# Question 7: Count the items in a list
# ==============================

numbers = [10, 20, 30, 40, 50]
count = 0

for number in numbers:
    count += 1

print("Count:", count)


# ==============================
# Question 8: Print numbers from 1 to 5 using while
# ==============================

i = 1

while i <= 5:
    print(i)
    i += 1


# ==============================
# Question 9: Find the sum of even numbers from 1 to 10
# ==============================

total = 0

for i in range(2, 11, 2):
    total += i

print("Sum of even numbers:", total)


# ==============================
# Question 10: Print each character in a string
# ==============================

word = "Python"

for character in word:
    print(character)


# ==============================
# Question 11: Count characters in a string
# ==============================

word = "Python"
count = 0

for character in word:
    count += 1

print("Character count:", count)


# ==============================
# Question 12: Calculate the factorial of 5
# ==============================

factorial = 1

for i in range(1, 6):
    factorial *= i

print("Factorial:", factorial)


# ==============================
# Question 13: Print squares of numbers from 1 to 5
# ==============================

for i in range(1, 6):
    print(i, "square =", i * i)


# ==============================
# Question 14: Find the sum of numbers in a list
# ==============================

numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number

print("List sum:", total)


# ==============================
# Question 15: Print multiples of 3 from 3 to 30
# ==============================

for i in range(3, 31, 3):
    print(i)


# ==============================
# Question 16: Find the product of numbers from 1 to 5
# ==============================

product = 1

for i in range(1, 6):
    product *= i

print("Product:", product)


# ==============================
# Question 17: Find the sum from 1 to 5 using while
# ==============================

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Sum:", total)


# ==============================
# Question 18: Keep asking for a number until 0 is entered
# ==============================

number = -1

while number != 0:
    number = int(input("Enter a number (0 to stop): "))

print("Loop ended")


# ==============================
# Question 19: Find the sum of user-entered numbers until 0
# ==============================

total = 0
number = -1

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    total += number

print("Total sum:", total)


# ==============================
# Question 20: Print numbers from 1 to 10 using while
# ==============================

i = 1

while i <= 10:
    print(i)
    i += 1
    
# ==============================