# Day 3 Python Revision Challenge

# ============================================================

# Q1. Variables

# Create variables to store your name, age, and CGPA.
# Print all three values.

name = input("Enter name : ")
age = int(input("Enter age : "))
cgpa = float(input("Enter CGPA : "))
print("name :", name)
print("age :", age)
print("CGPA :", cgpa)

# ============================================================

# Q2. Data Types

# Create variables with int, float, str, and bool values.
# Print the data type of each variable using type().

x = 10
y = 5.5
z = "Varsha"
a = True
b = False
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
# ============================================================

# Q3. User Input

# Take your name as input and print a welcome message.

name = input("Enter name : ")
print(f"Hi {name}, Good Morning!")

# ============================================================

# Q4. Type Conversion

# Store the value 25 in a variable.
# Convert it into a float and print the result.

num = 25
x = float(num)
print(x)

# ============================================================

# Q5. Type Conversion

# Store the value 15.8 in a variable.
# Convert it into an integer and print the result.

num = 15.8
x = int(num)
print(x)
# ============================================================

# Q6. Addition

# Take two numbers as input.
# Convert them into integers and print their sum.

num1 = input("Enter Number1 : ")
num2 = input("Enter Number2 : ")
total = int(num1) + int(num2)
print("Total = ", total)

# ============================================================

# Q7. Arithmetic Operators

# Given: a = 20 and b = 6
# Print the addition, subtraction, multiplication, and division.

a = 20
b = 6
print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)

# ============================================================

# Q8. Modulus Operator (%)

# Given: a = 27 and b = 5
# Find and print the remainder.

a = 27
b = 5
print("Remainder =", a % b)

# ============================================================

# Q9. Floor Division (//)

# Given: a = 27 and b = 5
# Find and print the quotient using floor division.

a = 27
b = 5
print("Quotient :", a//b)

# ============================================================

# Q10. Exponentiation (**)

# Given: number = 4
# Print its square and cube using the ** operator.

number = 4
print("Square =", number ** 2)
print("Cube =", number ** 3)

# ============================================================

# Q11. String Concatenation

# Store your first name and last name in separate variables.
# Join them with a space and print your full name.

first_name = input("Enter First_Name : ")
last_name = input("Enter last_Name : ")
print(first_name +" "+ last_name)

# ============================================================

# Q12. String Length

# Given: text = "Python Programming"
# Find and print the length of the string using len().

text = "Python Programming"
print("Length =", len(text))

# ============================================================

# Q13. String Methods

# Given: text = "python programming"
# Print the string in uppercase and title case.

text = "python programming"
print("Uppercase =", text.upper())
print("Title =", text.title())

# ============================================================

# Q14. Rectangle Calculation

# Given: length = 10 and breadth = 5
# Calculate and print the area and perimeter.

length = 10
breadth = 5
print("Area =", length * breadth)
print("Perimeter =", 2 * (length + breadth))

# ============================================================

# Q15. Simple Interest

# Given: principal = 1000, rate = 5, time = 2
# Calculate and print the simple interest.

principal = 1000
rate = 5
time = 2
print("Simple Interest =", (principal * rate * time) / 100)

# ============================================================
