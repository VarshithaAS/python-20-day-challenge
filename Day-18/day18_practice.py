
# Day 18: Modules in Python


# ==============================
# Question 1: Import the math module
# Print the value of pi
# ==============================

import math

print(math.pi)


# ==============================
# Question 2: Find the square root of 64
# ==============================

import math

print(math.sqrt(64))


# ==============================
# Question 3: Find the factorial of 5
# ==============================

import math

print(math.factorial(5))


# ==============================
# Question 4: Find the power of a number
# Calculate 2 raised to 3
# ==============================

import math

print(math.pow(2, 3))


# ==============================
# Question 5: Round a number upward
# ==============================

import math

print(math.ceil(4.3))


# ==============================
# Question 6: Round a number downward
# ==============================

import math

print(math.floor(4.8))


# ==============================
# Question 7: Generate a random integer
# Generate a number between 1 and 10
# ==============================

import random

print(random.randint(1, 10))


# ==============================
# Question 8: Select a random item
# ==============================

import random

fruits = ["Apple", "Mango", "Orange", "Banana"]

print(random.choice(fruits))


# ==============================
# Question 9: Get the current date and time
# ==============================

import datetime

current_time = datetime.datetime.now()

print(current_time)


# ==============================
# Question 10: Import only one function
# Find the square root of 81
# ==============================

from math import sqrt

print(sqrt(81))


# ==============================
# Question 11: Use an alias for a module
# ==============================

import math as m

print(m.sqrt(100))


# ==============================
# Question 12: Find the absolute value
# ==============================

import math

print(math.fabs(-25))


# ==============================
# Question 13: Calculate the greatest common divisor
# ==============================

import math

print(math.gcd(12, 18))


# ==============================
# Question 14: Shuffle a list
# ==============================

import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)


# ==============================
# Question 15: Find the remainder
# using the math module
# ==============================

import math

print(math.fmod(10, 3))


# ==============================
# Question 16: Create your own module
# Import a function from another Python file
# ==============================

# Create a file named mymodule.py
# Add this code inside it:
#
# def greet():
#     print("Hello, Python!")
#
# In day18_practice.py, write:

import mymodule

mymodule.greet()


# ==============================
# Question 17: Import multiple functions
# ==============================

from math import sqrt, factorial

print(sqrt(49))
print(factorial(4))


# ==============================
# Question 18: Find the maximum value
# using the built-in max() function
# ==============================

numbers = [10, 25, 5, 40, 15]

print(max(numbers))


# ==============================
# Question 19: Find the minimum value
# using the built-in min() function
# ==============================

numbers = [10, 25, 5, 40, 15]

print(min(numbers))


# ==============================
# Question 20: Display available names
# in the math module
# ==============================

import math

print(dir(math))

# ==============================
