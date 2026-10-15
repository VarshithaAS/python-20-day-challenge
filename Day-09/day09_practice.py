
# Day 09: Break, Continue and Nested Loops


# ==============================
# Question 1: Stop the loop at 5
# ==============================

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# ==============================
# Question 2: Skip number 5
# ==============================

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# ==============================
# Question 3: Print numbers 1 to 5
# using a while loop and break
# ==============================

i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


# ==============================
# Question 4: Skip even numbers
# ==============================

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# ==============================
# Question 5: Print a 3 x 3 pattern
# ==============================

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()


# ==============================
# Question 6: Print a right triangle
# ==============================

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# ==============================
# Question 7: Print this number pattern
# 1
# 1 2
# 1 2 3
# ==============================

for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ==============================
# Question 8: Print numbers 1 to 10,
# stopping when the number is greater than 7
# ==============================

for i in range(1, 11):
    if i > 7:
        break
    print(i)


# ==============================
# Question 9: Skip multiples of 3
# ==============================

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)


# ==============================
# Question 10: Print a square of numbers
# 1 1 1
# 2 2 2
# 3 3 3
# ==============================

for i in range(1, 4):
    for j in range(3):
        print(i, end=" ")
    print()

#==============================