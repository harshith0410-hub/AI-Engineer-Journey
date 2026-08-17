print("---------Mark Analyzer---------")
n=int(input("Enter the number of students: "))
marks=[]

for i in range(n):
    name=input("Enter the student's name: ")
    mark=int(input("Enter the student's mark: "))
    marks.append((name,mark))

student={key : value for key,value in marks}
print("\nStudent Marks:")
for name, mark in student.items():
    print(f"{name}: {mark}")

highest = max(student.items(), key=lambda x: x[1])
print("Highest Mark:", highest[0], "-", highest[1])

lowest = min(student.items(), key=lambda x: x[1])
print("Lowest Mark:", lowest[0], "-", lowest[1])

average = sum(student.values())/len(student)
print("Average Mark:", average)

print("Students who scored above 80:")

above_80={key : value for key,value in student.items() if value>80}
for name, mark in above_80.items():
    print(f"{name}: {mark}")

print("Students who scored below 40:")
below_40={key : value for key,value in student.items() if value<40}
for name, mark in below_40.items():
    print(f"{name}: {mark}")

