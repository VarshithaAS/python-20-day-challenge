# Day 5 Python Challenge
# Topic: Tuples

# ============================================================

# Q1. Creating a Tuple
# Create a tuple containing three colors and print it.

colors = ("red", "blue", "green")
print(colors)

# ============================================================

# Q2. Accessing Tuple Elements
# Print the first and third elements.

numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[2])

# ============================================================

# Q3. Negative Indexing
# Print the last element using negative indexing.

fruits = ("apple", "banana", "mango", "orange")
print(fruits[-1])

# ============================================================

# Q4. Tuple Length
# Find the number of elements using len().

values = (5, 10, 15, 20, 25)
print(len(values))

# ============================================================

# Q5. Checking an Element
# Check whether Python is present in the tuple.

languages = ("Python", "Java", "C", "JavaScript")
print("Python" in languages)

# ============================================================

# Q6. Counting Elements
# Count how many times 2 appears.

nums = (1, 2, 2, 3, 2, 4)
print(nums.count(2))

# ============================================================

# Q7. Finding an Index
# Find the index of rabbit.

animals = ("dog", "cat", "rabbit", "cow")
print(animals.index("rabbit"))

# ============================================================

# Q8. Tuple Slicing
# Print elements from index 1 to index 3.

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:4])

# ============================================================

# Q9. Single-Element Tuple
# Create a tuple containing only 100.
# Print its value and data type.

number = (100,)
print(number)
print(type(number))

# ============================================================

# Q10. Tuple Concatenation
# Join two tuples and print the result.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print(result)

# ============================================================

# Q11. Tuple Repetition
# Repeat the tuple three times.

numbers = (1, 2, 3)
print(numbers * 3)

# ============================================================

# Q12. Tuple Unpacking
# Store the tuple elements in separate variables.

student = ("Varshitha", 20, 8.25)
name, age, cgpa = student

print(name)
print(age)
print(cgpa)

# ============================================================

# Q13. Maximum and Minimum
# Find the maximum and minimum values.

numbers = (45, 12, 78, 23, 9)
print("Maximum =", max(numbers))
print("Minimum =", min(numbers))

# ============================================================

# Q14. Tuple Addition
# Add two tuples using the + operator.

a = (10, 20)
b = (30, 40)

c = a + b
print(c)

# ============================================================

# Q15. Check Membership
# Check whether 30 and 60 are present.

numbers = (10, 20, 30, 40, 50)

print(30 in numbers)
print(60 in numbers)

# ============================================================
