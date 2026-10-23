# Day 17: OOP Concepts in Python


# ==============================
# Question 1: Create a class and object
# ==============================

class Student:
    def display(self):
        print("Welcome to Python OOP")


student1 = Student()
student1.display()


# ==============================
# Question 2: Use the __init__() method
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
# Question 3: Demonstrate Encapsulation
# ==============================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def display_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)
account.display_balance()


# ==============================
# Question 4: Demonstrate Inheritance
# ==============================

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog1 = Dog()
dog1.eat()
dog1.bark()


# ==============================
# Question 5: Demonstrate Method Overriding
# ==============================

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal1 = Animal()
dog1 = Dog()

animal1.sound()
dog1.sound()


# ==============================
# Question 6: Demonstrate Polymorphism
# ==============================

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# ==============================
# Question 7: Demonstrate Class Variables
# ==============================

class Student:
    college = "GITW"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", Student.college)


student1 = Student("Varshitha")
student1.display()


# ==============================
# Question 8: Demonstrate Multiple Objects
# ==============================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Anu", 25000)
employee2 = Employee("Ravi", 30000)

employee1.display()
employee2.display()


# ==============================
# Question 9: Demonstrate Abstraction
# ==============================

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)


rectangle1 = Rectangle(10, 5)
rectangle1.area()


# ==============================
# Question 10: Create a Simple Calculator Class
# ==============================

class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        if b != 0:
            print("Division:", a / b)
        else:
            print("Cannot divide by zero")


calculator = Calculator()

calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)

# ==============================