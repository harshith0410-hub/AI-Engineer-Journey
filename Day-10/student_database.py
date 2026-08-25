import json

def load_students():
    try:
        with open('student_database.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students(students):
    with open("student_database.json", "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()

    name = input("Name: ")
    branch = input("Branch: ")
    marks = int(input("Marks: "))

    students.append({
        "name": name,
        "branch": branch,
        "marks": marks
    })

    save_students(students)
    print("Student added!")            

def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"Name: {s['name']}")
        print(f"Branch: {s['branch']}")
        print(f"Marks: {s['marks']}")
        print("-"*20)

def search_student():
    students = load_students()
    name = input("Enter name: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print(s)
            return

    print("Student not found.")

def delete_student():
    students = load_students()
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_students(students)
            print("Deleted.")
            return

    print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")                
