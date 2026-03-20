
data_students = {}

def adding():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    id = len(data_students) + 1
    
    data_students[id] = {
        'name': name,
        'age': age,
        'grade': grade
    }
    print(f"Student {name} added with ID: {id}")

def details(id):
    student = data_students.get(id)
    if student:
        print(f"Student ID: {id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
    else:
        print("Student not found!")



def deletinginfo(id):
    if id in data_students:
        del data_students[id]
        print(f"Student with ID {id} removed.")
    else:
        print("Student not found!")
def showalldata():
    print("Student List:")
    for id, student in data_students.items():
        print(f"ID: {id}, Name: {student['name']}")
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Student Details")
        print("3. Display All Students")
        print("4. Remove Student")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            adding()
        elif choice == 2:
            student_id = int(input("Enter student ID: "))
            details(student_id)
        elif choice == 3:
            showalldata()
        elif choice == 4:
            student_id = int(input("Enter student ID: "))
            deletinginfo(student_id)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()




