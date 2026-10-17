
# Day 11: Functions in Python


# ==============================
# Question 1: Create a function to print Hello World
# ==============================

def greet():
    print("Hello World")

greet()


# ==============================
# Question 2: Create a function to print your name
# ==============================

def display_name():
    print("My name is Varshitha")

display_name()


# ==============================
# Question 3: Create a function to add two numbers
# ==============================

def add():
    a = 10
    b = 20
    print("Sum:", a + b)

add()


# ==============================
# Question 4: Create a function to subtract two numbers
# ==============================

def subtract():
    a = 50
    b = 20
    print("Difference:", a - b)

subtract()


# ==============================
# Question 5: Create a function to multiply two numbers
# ==============================

def multiply():
    a = 5
    b = 4
    print("Product:", a * b)

multiply()


# ==============================
# Question 6: Create a function to check even or odd
# ==============================

def check_even_odd():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd()


# ==============================
# Question 7: Create a function with one parameter
# to greet a person
# ==============================

def greet_person(name):
    print("Hello", name)

greet_person("Varshitha")


# ==============================
# Question 8: Create a function to find the square
# of a number using a parameter
# ==============================

def square(num):
    print("Square:", num * num)

square(5)


# ==============================
# Question 9: Create a function to find the area
# of a rectangle
# ==============================

def rectangle_area(length, width):
    print("Area:", length * width)

rectangle_area(10, 5)


# ==============================
# Question 10: Create a function to find the largest
# of two numbers
# ==============================

def find_largest(a, b):
    if a > b:
        print("Largest:", a)
    elif b > a:
        print("Largest:", b)
    else:
        print("Both numbers are equal")

find_largest(25, 40)


# ==============================
# Question 11: Create a function to calculate
# simple interest
# ==============================

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print("Simple Interest:", interest)

simple_interest(10000, 5, 2)


# ==============================
# Question 12: Create a function to check
# whether a number is positive, negative or zero
# ==============================

def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-5)


# ==============================
# Question 13: Create a function to count
# numbers in a list
# ==============================

def count_numbers(numbers):
    print("Count:", len(numbers))

count_numbers([10, 20, 30, 40, 50])


# ==============================
# Question 14: Create a function to find
# the sum of numbers in a list
# ==============================

def sum_numbers(numbers):
    total = 0

    for num in numbers:
        total = total + num

    print("Sum:", total)

sum_numbers([10, 20, 30, 40])


# ==============================
# Question 15: Create a function to count
# even numbers in a list
# ==============================

def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count = count + 1

    print("Even count:", count)

count_even([1, 2, 3, 4, 5, 6])


# ==============================
# Question 16: Create a function to print
# a multiplication table
# ==============================

def multiplication_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

multiplication_table(7)


# ==============================
# Question 17: Create a function to find
# the largest number in a list
# ==============================

def find_largest_number(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print("Largest number:", largest)

find_largest_number([12, 45, 23, 67, 34])


# ==============================
# Question 18: Create a function to calculate
# the average of three numbers
# ==============================

def calculate_average(a, b, c):
    average = (a + b + c) / 3
    print("Average:", average)

calculate_average(10, 20, 30)


# ==============================
# Question 19: Create a function to check
# whether a number is divisible by 5
# ==============================

def divisible_by_five(num):
    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

divisible_by_five(25)


# ==============================
# Question 20: Create a function to calculate
# the total of positive numbers in a list
# ==============================

def sum_positive(numbers):
    total = 0

    for num in numbers:
        if num > 0:
            total = total + num

    print("Total of positive numbers:", total)

sum_positive([10, -5, 20, -3, 15])

# ==============================