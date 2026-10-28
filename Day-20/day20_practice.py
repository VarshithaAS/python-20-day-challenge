
# Day 20: Python Revision and Mini Project
# Project: Student Marks Management System


students = {}


# ==============================
# Function 1: Add a student
# ==============================

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        students[name] = marks
        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric marks.")


# ==============================
# Function 2: Calculate grade
# ==============================

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 35:
        return "D"
    else:
        return "Fail"


# ==============================
# Function 3: View all students
# ==============================

def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for name, marks in students.items():
        grade = calculate_grade(marks)

        print(
            f"Name: {name} | "
            f"Marks: {marks:g} | Grade: {grade}"
        )


# ==============================
# Function 4: Search for a student
# ==============================

def search_student():
    name = input("Enter student name to search: ").strip()

    if name in students:
        marks = students[name]
        grade = calculate_grade(marks)

        print("Name:", name)
        print("Marks:", marks)
        print("Grade:", grade)
    else:
        print("Student not found.")


# ==============================
# Function 5: Calculate class average
# ==============================

def calculate_average():
    if not students:
        print("No marks available.")
        return

    total = sum(students.values())
    average = total / len(students)

    print(f"Class average: {average:.2f}")


# ==============================
# Main Program
# ==============================

while True:
    print("\n===== Student Marks Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            calculate_average()

        elif choice == 5:
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Select 1 to 5.")

    except ValueError:
        print("Please enter a valid menu number.")

# =====================================================