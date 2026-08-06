n=int(input("Enter the number of students: "))
students=[]
for i in range(n):
    print("Enter student {} details:".format(i+1))
    marks=[]
    for j in range(6):
        m=int(input("Enter marks for subject {}: ".format(j+1)))
        marks.append(m)
    students.append(marks)    
print("\n----- Student Details -----")
for i in range(n):
    print("Student {} marks: {}".format(i+1, students[i]))
for i in range(n):
    m=max(students[i])
    print("Maximum marks for student {}: {}".format(i+1, m))
    n=min(students[i])
    print("Minimum marks for student {}: {}".format(i+1, n))
    avg=sum(students[i])/len(students[i])
    print("Average marks for student {}: {}".format(i+1, avg))
    if avg<35:
        print("Student {} has failed.".format(i+1))
    else:
        print("Student {} has passed.".format(i+1))        