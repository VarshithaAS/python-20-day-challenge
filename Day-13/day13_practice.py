# Day 13: Python Comprehensions

# ==============================
# Question 1: Create a list of numbers from 1 to 10 using list comprehension
# ==============================

numbers = [i for i in range(1, 11)]
print(numbers)


# ==============================
# Question 2: Create a list of even numbers from 1 to 20
# ==============================

even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(even_numbers)


# ==============================
# Question 3: Create a list of squares from 1 to 10
# ==============================

squares = [i ** 2 for i in range(1, 11)]
print(squares)


# ==============================
# Question 4: Create a list of odd numbers from 1 to 15
# ==============================

odd_numbers = [i for i in range(1, 16) if i % 2 != 0]
print(odd_numbers)


# ==============================
# Question 5: Convert all names to uppercase
# ==============================

names = ["varshitha", "priya", "ananya"]

uppercase_names = [name.upper() for name in names]
print(uppercase_names)


# ==============================
# Question 6: Create a list of numbers greater than 5
# ==============================

numbers = [2, 4, 6, 8, 10, 3, 7]

result = [i for i in numbers if i > 5]
print(result)


# ==============================
# Question 7: Create a list of cubes from 1 to 5
# ==============================

cubes = [i ** 3 for i in range(1, 6)]
print(cubes)


# ==============================
# Question 8: Extract words containing more than 4 characters
# ==============================

words = ["apple", "cat", "banana", "dog", "grapes"]

result = [word for word in words if len(word) > 4]
print(result)


# ==============================
# Question 9: Create a list of positive numbers
# ==============================

numbers = [-5, 10, -2, 8, 0, 3]

positive_numbers = [i for i in numbers if i > 0]
print(positive_numbers)


# ==============================
# Question 10: Replace negative numbers with zero
# ==============================

numbers = [-3, 5, -1, 7, -8]

result = [0 if i < 0 else i for i in numbers]
print(result)

# ==============================