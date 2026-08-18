print("--------- Student Record System ---------")
print("Welcome to the Student Record System!")

num_students = int(input("Enter the number of students you want to add: "))

for i in range(num_students):

    print(f"\nEnter the details of student {i + 1}:")

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = input("Enter marks: ")

    with open("student_record.txt", "a") as f:
        f.write(f"Student {i + 1}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Branch: {branch}\n")
        f.write(f"Marks: {marks}\n")

    print(f"Student {i + 1} added successfully!")


# ---------------- VIEW STUDENTS ----------------

print("\n--------- Student Details ---------")

with open("student_record.txt", "r") as f:
    lines = f.readlines()

if len(lines) == 0:
    print("No students available.")

else:
    for line in lines:
        print(line.strip())


# ---------------- SEARCH STUDENT ----------------

print("\nEnter the student name you want to search:")
student_name = input()

with open("student_record.txt", "r") as f:
    lines = f.readlines()

found = False

for i in range(len(lines)):

    if lines[i].startswith("Name: " + student_name):

        print("\n--------- Student Found ---------")

        print(lines[i - 2].strip())  # Student number
        print(lines[i].strip())      # Name
        print(lines[i + 1].strip())  # Branch
        print(lines[i + 2].strip())  # Marks

        found = True
        break

if not found:
    print("Student not found.")