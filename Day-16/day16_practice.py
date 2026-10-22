# Day 16: Object-Oriented Programming (OOP) Basics in Python

# ==============================
# Question 1: Create a class named Student
# ==============================

class Student:
    pass


# ==============================
# Question 2: Create an object of the Student class
# ==============================

class Student:
    pass

student1 = Student()


# ==============================
# Question 3: Create a class with an attribute
# ==============================

class Student:
    name = "Varshitha"

student1 = Student()
print(student1.name)


# ==============================
# Question 4: Create a class with two attributes
# ==============================

class Student:
    name = "Varshitha"
    age = 21

student1 = Student()
print(student1.name)
print(student1.age)


# ==============================
# Question 5: Create a class with a method
# ==============================

class Student:
    def display(self):
        print("Welcome to Python")

student1 = Student()
student1.display()


# ==============================
# Question 6: Create a class with attributes and a method
# ==============================

class Student:
    name = "Varshitha"

    def display(self):
        print("Student Name:", self.name)

student1 = Student()
student1.display()


# ==============================
# Question 7: Use the __init__() constructor
# ==============================

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Varshitha")
print(student1.name)


# ==============================
# Question 8: Create an object with multiple attributes
# ==============================

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Varshitha", 21)

print(student1.name)
print(student1.age)


# ==============================
# Question 9: Create a method to display student details
# ==============================

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Varshitha", 21)
student1.display()


# ==============================
# Question 10: Create two objects of the same class
# ==============================

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Varshitha")
student2 = Student("Ananya")

print(student1.name)
print(student2.name)

# ==============================