# Day 10: Conditions and Loops in Python


# ==============================
# Question 1: Print numbers from 1 to 20
# ==============================

for i in range(1, 21):
    print(i)


# ==============================
# Question 2: Print even numbers from 1 to 50
# ==============================

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# ==============================
# Question 3: Skip multiples of 3 from 1 to 20
# ==============================

for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


# ==============================
# Question 4: Check whether numbers are even or odd
# ==============================

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")


# ==============================
# Question 5: Find the sum of numbers from 1 to 10
# ==============================

total = 0

for i in range(1, 11):
    total = total + i

print("Sum:", total)


# ==============================
# Question 6: Print numbers from 10 down to 1
# ==============================

for i in range(10, 0, -1):
    print(i)


# ==============================
# Question 7: Print numbers divisible by both 3 and 5
# ==============================

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# ==============================
# Question 8: Count even numbers from 1 to 20
# ==============================

count = 0

for i in range(1, 21):
    if i % 2 == 0:
        count = count + 1

print("Count of even numbers:", count)


# ==============================
# Question 9: Find the sum of odd numbers from 1 to 50
# ==============================

total = 0

for i in range(1, 51):
    if i % 2 != 0:
        total = total + i

print("Sum of odd numbers:", total)


# ==============================
# Question 10: Print the multiplication table
# ==============================

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# ==============================    