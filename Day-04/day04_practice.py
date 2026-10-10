
# ==========================================
# Python 20-Day Challenge
# Day 04 - Python Lists
# ==========================================


# Q1. Creating a List
# Create a list named languages containing
# "Python", "Java", and "C++".
# Print the entire list.

languages = ["Python", "Java", "C++"]
print(languages)

# ==========================================

# Q2. Positive Indexing
# Given: fruits = ["apple", "banana", "mango", "orange"]
# Print the first element, third element,
# and last element.

fruits = ["apple", "banana", "mango", "orange"]
print("first element =", fruits[0])
print("third element =", fruits[2])
print("last element =", fruits[-1])

# ==========================================

# Q3. Negative Indexing
# Given: numbers = [10, 20, 30, 40, 50]
# Print the last element and second-last element.

numbers = [10, 20, 30, 40, 50]
print("last element =", numbers[-1])
print("second-last element =", numbers[-2])
# ==========================================

# Q4. Updating List Elements
# Given: colors = ["red", "blue", "green"]
# Change "blue" to "yellow".
# Print the updated list.

colors = ["red", "blue", "green"]
colors[1]="yellow"
print(colors)

# ==========================================

# Q5. Adding Elements
# Given: animals = ["cat", "dog"]
# Add "rabbit" using append().
# Print the updated list.

animals = ["cat", "dog"]
animals.append("rabbit")
print(animals)

# ==========================================

# Q6. Inserting Elements
# Given: numbers = [10, 20, 40, 50]
# Insert 30 at index 2 using insert().
# Print the updated list.

numbers = [10, 20, 40, 50]
numbers.insert(2,30)
print(numbers)

# ==========================================

# Q7. Removing Elements
# Given: fruits = ["apple", "banana", "mango"]
# Remove "banana" using remove().
# Print the updated list.

fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)


# ==========================================

# Q8. List Length
# Given: marks = [85, 90, 78, 92, 88]
# Find and print the number of elements using len().

marks = [85, 90, 78, 92, 88]
print("The number of elements =", len(marks))

# ==========================================

# Q9. List Slicing
# Given: numbers = [10, 20, 30, 40, 50, 60]
# Print the first three elements.
# Print the list in reverse order.

numbers = [10, 20, 30, 40, 50, 60]
print("first three elements =", numbers[:3])
print("list in reverse order =", numbers[::-1])

# ==========================================

# Q10. Sum and Average
# Given: marks = [80, 75, 90, 85, 70]
# Calculate and print the sum and average of the marks.

marks = [80, 75, 90, 85, 70]
total = sum(marks)
average = total / len(marks)
print("total =", total)
print("average =", average)

# ==========================================

# Q11. Find the Largest Number
# Given: numbers = [12, 45, 23, 67, 34]
# Find and print the largest number in the list.

numbers = [12, 45, 23, 67, 34]
print(max(numbers))

# ==========================================

# Q12. Check Whether an Element Exists
# Given: numbers = [10, 20, 30, 40, 50]
# Check whether 30 exists in the list using 'in'.
# Print the result.

numbers = [10, 20, 30, 40, 50]
print(30 in numbers)

# ==========================================

# Q13. Sort a List
# Given: numbers = [40, 10, 50, 20, 30]
# Sort the list in ascending order using sort().
# Print the sorted list.

numbers = [40, 10, 50, 20, 30]
numbers.sort()
print("List in ascending order =", numbers)

# ==========================================

# Q13. Sort a List in Descending Order
# Given: numbers = [25, 10, 45, 5, 30]
# Sort the list from largest to smallest using sort().
# Print the sorted list.

numbers = [25, 10, 45, 5, 30]
numbers.sort(reverse=True)
print("list from largest to smallest =", numbers) 

# ==========================================

# Q14. List Challenge — Find Unique Numbers
# Given a list containing duplicate numbers:
numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

# 1. Remove duplicate numbers.
# 2. Sort the remaining numbers in descending order.
# 3. Print the final list.

# Expected Output:
# [60, 50, 40, 30, 20, 10]

numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]
numbers = list(set(numbers))
numbers.sort(reverse = True)
print(numbers)

# ==========================================

# Q15. List Challenge
# Given a list containing duplicate numbers:
numbers = [25, 10, 45, 25, 60, 10, 80, 45, 70, 60]

# 1. Remove duplicate numbers.
# 2. Sort the list in descending order.
# 3. Print the largest number.
# 4. Print the top 3 largest unique numbers using slicing.

numbers = [25, 10, 45, 25, 60, 10, 80, 45, 70, 60]
numbers = list(set(numbers))
numbers.sort(reverse = True)
print("the largest number =", numbers[0])
print("the top 3 largest unique numbers =", numbers[:3])
