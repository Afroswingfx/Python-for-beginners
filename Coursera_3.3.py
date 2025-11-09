# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
# try:
#     grade = float(input("Enter Grade (between 0.0 and 1.0): "))
#     if grade < 0.0 or grade > 1.0:
#         print("Error: Grade must be between 0.0 and 1.0")
#     elif grade >= 0.9:
#         print("A")
#     elif grade >= 0.8:
#         print("B")
#     elif grade >= 0.7:
#         print("C")
#     elif grade >= 0.6:
#         print("D")
#     else:
#         print("F")
# except ValueError:
#     print("Error: Please enter a valid number")
# grade=float(input("Enter grade, must be between 0.0 and 1.0: "))
# if grade <+0.0 or grade >1.0:
#     print("Grade error")
# elif grade>=0.9:
#     print("A")
# elif grade >=0.8:
#     print("B")
# elif grade>=0.7:
#     print("C")
# elif grade>=0.6:
#     print("D")
# elif grade >0.0 and grade < 0.6:
#     print("F")
# else:
#     print("Grade error")
grade = float(input("Enter grade, must be between 0.0 and 1.0: "))
if grade < 0.0 or grade > 1.0:  # Changed 'and' to 'or'
    print("Grade error")
elif grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:  # This handles 0.0 to < 0.6
    print("F")