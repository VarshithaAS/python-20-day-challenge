
# Day 06: Sets in Python
# Topic: Set Operations

#====================================================

# Question 1: Create a Set
numbers = {10, 20, 30, 20, 40, 10}
print("Set:", numbers)

#====================================================

# Question 2: Add an Element
numbers = {10, 20, 30}
numbers.add(50)
print("After adding:", numbers)

#====================================================

# Question 3: Remove an Element
numbers = {10, 20, 30, 40}
numbers.remove(20)
print("After removing:", numbers)

#====================================================

# Question 4: Find the Length of a Set
numbers = {10, 20, 30, 40, 50}
print("Length:", len(numbers))

#====================================================

# Question 5: Check Membership
numbers = {10, 20, 30, 40}
print("Is 30 present?", 30 in numbers)

#====================================================

# Question 6: Remove Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

#====================================================

# Question 7: Union of Two Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))

#====================================================

# Question 8: Intersection of Two Sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("Intersection:", set1.intersection(set2))

#====================================================

# Question 9: Difference of Two Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Difference:", set1.difference(set2))

#====================================================

# Question 10: Clear a Set
numbers = {10, 20, 30, 40}
numbers.clear()
print("After clearing:", numbers)

#====================================================