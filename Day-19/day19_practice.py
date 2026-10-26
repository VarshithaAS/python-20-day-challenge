# Day 19: Iterators and Generators in Python


# ==============================
# Question 1: Create an iterator from a list
# ==============================

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))


# ==============================
# Question 2: Print the first three elements using an iterator
# ==============================

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==============================
# Question 3: Create a generator that produces numbers from 1 to 5
# ==============================

def generate_numbers():
    for i in range(1, 6):
        yield i

for num in generate_numbers():
    print(num)


# ==============================
# Question 4: Create a generator that produces even numbers from 2 to 10
# ==============================

def even_numbers():
    for i in range(2, 11, 2):
        yield i

for num in even_numbers():
    print(num)


# ==============================
# Question 5: Create a generator that produces squares from 1 to 5
# ==============================

def squares():
    for i in range(1, 6):
        yield i * i

for square in squares():
    print(square)


# ==============================
# Question 6: Create a generator that produces numbers from 10 to 1
# ==============================

def countdown():
    for i in range(10, 0, -1):
        yield i

for num in countdown():
    print(num)


# ==============================
# Question 7: Create a generator that produces multiples of 5 from 5 to 50
# ==============================

def multiples_of_five():
    for i in range(5, 51, 5):
        yield i

for num in multiples_of_five():
    print(num)


# ==============================
# Question 8: Create a generator that produces cubes from 1 to 5
# ==============================

def cubes():
    for i in range(1, 6):
        yield i ** 3

for cube in cubes():
    print(cube)


# ==============================
# Question 9: Use an iterator to access list elements one by one
# ==============================

fruits = ["Apple", "Banana", "Mango"]

iterator = iter(fruits)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==============================
# Question 10: Create a generator that produces odd numbers from 1 to 19
# ==============================

def odd_numbers():
    for i in range(1, 20, 2):
        yield i

for num in odd_numbers():
    print(num)

# ==============================