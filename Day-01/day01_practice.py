# ==========================================
# Python 20-Day Challenge
# Day 01 - Python Basics
# ==========================================


# Question 1: Variables

name = "Varshitha"
age = 20
cgpa = 8.25

print(name)
print(age)
print(cgpa)


# Question 2: Multiple Variables

name, age, cgpa = "Varshitha", 20, 8.25

print(name)
print(age)
print(cgpa)


# Question 3: Same Value to Multiple Variables

a = b = c = 100

print(a)
print(b)
print(c)


# Question 4: Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")


# Question 5: Arithmetic Operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)


# Question 6: Rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area:", area)
print("Perimeter:", perimeter)


# Question 7: Marks

mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))
mark3 = float(input("Enter third subject mark: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Total:", total)
print("Average:", average)


# Question 8: Temperature

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)


# Question 9: Swapping

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# Question 10: Strings

word = input("Enter a word: ")

print("First character:", word[0])
print("Last character:", word[-1])
print("Length:", len(word))
print("Uppercase:", word.upper())
print("Lowercase:", word.lower())