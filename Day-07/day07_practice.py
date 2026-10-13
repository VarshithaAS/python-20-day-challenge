# Day 07: Dictionary Practice
# Topic: Dictionaries in Python

#======================================================

# Question 1:
# Create a dictionary named student with name, age, and branch.

student = {
    "name": "Varshitha",
    "age": 20,
    "branch": "CSE"
}

print(student)

#======================================================

# Question 2:
# Print the name from the student dictionary.

print(student["name"])

#======================================================

# Question 3:
# Print the age using the get() method.

print(student.get("age"))

#======================================================

# Question 4:
# Change the student's age to 21.

student["age"] = 21
print(student)

#======================================================

# Question 5:
# Add a new key "city" with the value "Bengaluru".

student["city"] = "Bengaluru"
print(student)

#======================================================

# Question 6:
# Remove the "branch" key from the dictionary.

student.pop("branch")
print(student)

#======================================================

# Question 7:
# Print all keys in the student dictionary.

print(student.keys())

#======================================================

# Question 8:
# Print all values in the student dictionary.

print(student.values())

#======================================================

# Question 9:
# Update the city to "Mysuru" using update().

student.update({"city": "Mysuru"})
print(student)

#======================================================

# Question 10:
# Create a dictionary named marks with three subjects
# and their marks. Print the marks for Python.

marks = {
    "Python": 90,
    "Maths": 85,
    "DSA": 88
}

print(marks["Python"])

#======================================================