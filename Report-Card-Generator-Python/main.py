# -------------------------------------------------------------
# More LIST METHODS
'''
list_a = [10, 20, 30, 40, 30]
count = list_a.count(30)
print(count) # Output: 2

index = list_a.index(40)
print(index) # Output: 3

list_a.remove(4)
print(list_a) # [1, 2]

list_a.sort()
print(list_a) # [10, 20, 30, 30, 40]

list_a = [10, 20, 30, 40, 30]
sorted_list = sorted(list_a)
print(sorted_list)  # [10, 20, 30, 30, 40]

list_a.reverse()
print(list_a) # [30, 40, 30, 20, 10]

list_a.clear()
print(list_a) # []
'''

# More Built-in Functions:
'''
smallest= min(3,5,4)
print(smallest)
# Output: 3

smallest = min([1,-2,4,2])
print(smallest)
# Output: -2
'''


# -------------------------------------------------------------
# REPORT CARD GENERATOR PROGRAM

print("### Welcome to Report Card Generator ###\n")

# Subjects taught in school
all_subjects = ["Math", "Science", "English", "History"]

# Create an empty report card list to store all student records
report_cards = []

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Collect student names and marks for each subject
for i in range(num_students):
  student_name = input(f"\nEnter name for student {i + 1}: ")
  marks = []
  print(f"Please provide {student_name}'s grades for the following subjects:")
  for subject in all_subjects:
    grade = int(input(f"{subject}: "))
    marks.append(grade)

  # Pack the name and marks together and add it to the report_cards list
  student_record = [student_name] + marks
  report_cards.append(student_record)

# Display the final report cards for each student
print("\n--------------------------------------")
print("Congratulations to all students!")
print("Here are your final School Report Cards:")

# Display the report card with grades
print("\nReport Cards:")
for student in report_cards:
  print(f"\nStudent Name: {student[0]}")
  for i in range(1, len(student)):
    print(f"{all_subjects[i-1]}: {student[i]}")

# Calculate the overall average for each student
print("\n--------------------------------------")
print("Overall Average:")

for student in report_cards:
  name = student[0]
  grades = student[1:]
  average = sum(grades) / len(grades)
  print(f"{name}: {average:.2f}")

# Display a Hall of Fame congratulating all students on the School Notice Board:
print("\n--------------------------------------")
print("HALL OF FAME:")
for student in report_cards:
  name = student[0]
  grades = student[1:]
  average = sum(grades) / len(grades)
  if average >= 80:
    print(f"{name}, the brilliant student, excelled in all subjects.")
  elif average >= 60:
    print(f"{name}, the hardworking student, showed steady progress.")
  else:
    print(f"{name}, the determined student, is working on improving.")

print("\nKeep up the good work! Learning is a lifelong adventure!")
print("Thanks for using the Report Card Generator!!")
