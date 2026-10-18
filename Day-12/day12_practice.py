
# Day 12: Return Values and Scope in Python


# ==============================
# Question 1: Return the sum of two numbers
# ==============================

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# ==============================
# Question 2: Return the square of a number
# ==============================

def square(n):
    return n * n

print(square(5))


# ==============================
# Question 3: Return the largest of two numbers
# ==============================

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(15, 10))


# ==============================
# Question 4: Return True if a number is even
# ==============================

def is_even(n):
    return n % 2 == 0

print(is_even(8))


# ==============================
# Question 5: Return the factorial of a number
# ==============================

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print(factorial(5))


# ==============================
# Question 6: Use a local variable
# ==============================

def display():
    message = "Hello Python"
    print(message)

display()


# ==============================
# Question 7: Use a global variable
# ==============================

name = "Varshitha"

def greet():
    print(name)

greet()


# ==============================
# Question 8: Return the length of a string
# ==============================

def string_length(text):
    return len(text)

print(string_length("Python"))


# ==============================
# Question 9: Return the average of three numbers
# ==============================

def average(a, b, c):
    return (a + b + c) / 3

print(average(10, 20, 30))


# ==============================
# Question 10: Return the sum of numbers from 1 to n
# ==============================

def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print(sum_numbers(10))

# ==============================
