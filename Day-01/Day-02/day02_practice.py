# ============================================================
# Day 02 - Python Strings
# ============================================================


# Q1. Creating a String
# Create a string using single quotes and another using
# double quotes. Print both.

word1 = 'python'
word2 = "programming"
print("string 1=", word1)
print("string 2=", word2)

# ============================================================

# Q2. len()
# Given: "Python Programming"
# Find and print the length of the string.

text = "Python Programming"
length = len(text)
print("The length of the string is", length)

# ============================================================

# Q3. Positive Indexing
# Given: "Python"
# Print the first, third, and last characters.

text = "Python"
print("first character=", text[0])
print("third character=", text[2])
print("last character=", text[5])

# ============================================================

# Q4. Negative Indexing
# Given: "Python"
# Print the last, second-last, and first characters
# using negative indexing.

word = "Python"
print("last character=", word[-1])
print("second-last character=", word[-2])
print("first character=", word[-6])

# ============================================================

# Q5. String Slicing
# Given: "Python Programming"
# Print:
# 1. "Python"
# 2. "Programming"
# 3. First 5 characters
# 4. Last 5 characters

word = "Python Programming"
print('"Python"=', word[:6])
print('"Programming"=', word[7:])
print("First 5 characters is", word[:5])
print("Last 5 characters is", word[13:])

# ============================================================

# Q6. String Slicing with Step
# Given: "Python"
# Print:
# 1. Every second character
# 2. The string in reverse

text = "Python"
print("Every second character=", text[0::2])
print("The string in reverse=", text[::-1])

# ============================================================

# Q7. String Concatenation (+)
# Take first name and last name from the user
# and create a full name using +.

first_name = input("Enter a first name:")
last_name = input("Enter the last name:")
print(first_name + " " + last_name)

# ============================================================

# Q8. String Repetition (*)
# Take a word from the user and print it 3 times using *.

word = input("Enter a word:")
print((word + " ") * 3)

# ============================================================

# Q9. upper() and lower()
# Take a string from the user and print:
# 1. Uppercase
# 2. Lowercase

word = input("Enter a string:")
print(word.upper())
print(word.lower())

# ============================================================

# Q10. capitalize() and title()
# Given: "python programming language"
# Print the result using:
# 1. capitalize()
# 2. title()

word = "python programming language"
print("capitalize=", word.capitalize())
print("title=", word.title())

# ============================================================

# Q11. strip()
# Given: "   Python Programming   "
# Remove spaces from the beginning and end.

word = "   Python Programming   "
print("Remove spaces from the beginning and end is", word.strip())

# ============================================================

# Q12. replace()
# Given: "I am learning Java"
# Replace "Java" with "Python".

text = "I am learning Java"
print(text.replace("Java", "Python"))

# ============================================================

# Q13. split()
# Given: "Python is easy to learn"
# Split the sentence into individual words.

sentence = "Python is easy to learn"
print(sentence.split())

# ============================================================

# Q14. input() + String Operations
# Take a name from the user and print:
# 1. Length
# 2. First character
# 3. Last character
# 4. Uppercase
# 5. Lowercase

name = input("Enter name:")
print("length of the name is=", len(name))
print("First character=", name[0])
print("last character=", name[-1])
print("Uppercase=", name.upper())
print("Lowercase=", name.lower())

# ============================================================

# Q15. Placement Practice 
# Take a word from the user and print the reverse
# of the word using slicing.

name = input("Enter word:")
print(name[::-1])

# ============================================================
