def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass(marks):
    for mark in marks:
        if mark < 35:
            return "FAIL"
    return "PASS"


name = input("Enter student name: ")
usn = input("Enter USN: ")
branch = input("Enter branch: ")

marks = []

python = float(input("Enter Python marks: "))
maths = float(input("Enter Mathematics marks: "))
dsa = float(input("Enter DSA marks: "))
cs = float(input("Enter Computer Science marks: "))
english = float(input("Enter English marks: "))

marks.append(python)
marks.append(maths)
marks.append(dsa)
marks.append(cs)
marks.append(english)

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)
result = check_pass(marks)

print("\n========== STUDENT REPORT ==========")

print("Name       :", name)
print("USN        :", usn)
print("Branch     :", branch)

print("\nPython     :", python)
print("Mathematics:", maths)
print("DSA        :", dsa)
print("Computer   :", cs)
print("English    :", english)

print("\nTotal      :", total)
print("Average    :", average)
print("Grade      :", grade)
print("Result     :", result)

print("====================================")