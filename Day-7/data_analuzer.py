class student:
    def __init__(self,name,branch,marks):
        self.name=name
        self.branch=branch
        self.marks=marks

    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)    

students=[]
print("---------Student Management System---------")
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter the student's name: ")
    branch=input("Enter the student's branch: ")
    marks=[]
    m=int(input("Enter the number of marks you want to add for this student: "))
    for j in range(m):
        mark=int(input("Enter the mark: "))
        marks.append(mark)
    s=student(name,branch,marks)
    students.append(s)

def highest_average(students):
    highest_avg=0
    top_student=None
    for s in students:
        avg=s.average_marks()
        if avg>highest_avg:
            highest_avg=avg
            top_student=s
    return top_student,highest_avg

def lowest_average(students):
    lowest_avg=float('inf')
    bottom_student=None
    for s in students:
        avg=s.average_marks()
        if avg<lowest_avg:
            lowest_avg=avg
            bottom_student=s
    return bottom_student,lowest_avg

def class_average(students):
    total=0
    count=0
    for s in students:
        total+=sum(s.marks)
        count+=len(s.marks)
    return total/count if count>0 else 0

print("==========Student Marks Analysis=========")

for s in students:
    print(f"{s.name}  -> {s.average_marks()}")

top_student, top_average = highest_average(students)
print("Highest Average:", top_student.name, "->", top_average)
bottom_student, bottom_average = lowest_average(students)
print("Lowest Average:", bottom_student.name, "->", bottom_average)
print("Class Average:", class_average(students))    