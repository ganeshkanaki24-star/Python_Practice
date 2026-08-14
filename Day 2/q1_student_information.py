# Scenario 1: College Student Profile

# You are creating a small student information system for your college.

# Ask the student for:

# Name
# Age
# Roll number
# Course
# College name
# Percentage

# Display all information in a properly formatted profile.

# Concepts: Variables, input(), strings, numbers, print().

Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Roll_number = int(input("Enter your roll number: "))
Course = input("Enter your course: ")
College_name = input("Enter your college name: ")
Percentage = float(input("Enter your percentage: "))

print("\nStudent Profile")
print("Name:", Name)
print("Age:", Age)
print("Roll Number:", Roll_number)
print("Course:", Course)
print("College Name:", College_name)
print("Percentage:", Percentage)