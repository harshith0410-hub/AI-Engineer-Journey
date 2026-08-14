class student:
    def __init__(self,name,age,branch,marks):
        self.name=name
        self.age=age
        self.branch=branch
        self.marks=marks

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Branch:",self.branch)
        print("Marks:",self.marks)


    def add_mark(self):
        n=int(input("Enter the number of marks you want to add: "))
        for i in range(n):
            marks=int(input("Enter the mark: "))
            self.marks.append(marks)


    def average_marks(self):
        if len(self.marks)==0:
            return 0
        return sum(self.marks)/len(self.marks)

students=[]
print("---------Student Management System---------")

while True:

    print("\nChoose an option you want to perform: ")
    print("1. Add Student")
    print("2. Display Student Information")
    print("3. Search Student by Name")        
    print("4. Exit")

    n=int(input("Enter your choice: "))

    if n==1:
      m=int(input("Enter the number of students you want to add: "))
      for j in range(m):
        name=input("Enter the student's name: ")
        age=int(input("Enter the student's age: "))
        branch=input("Enter the student's branch: ")
        marks=[]
        s=student(name,age,branch,marks)
        s.add_mark()
        students.append(s)

    elif n==2:
        n=int(input("Enter which student's information you want to display (1, 2, ...): "))
        if n<=len(students):
            students[n-1].display()
            print("Average Marks:",students[n-1].average_marks())
        else:
            print("Invalid choice. Please try again.")

    elif n==3:
        name=input("Enter the student's name you want to search: ")
        found=False
        for s in students:
            if s.name==name:
                s.display()
                print("Average Marks:",s.average_marks())
                found=True
                break
        if not found:
            print("Student not found.")

    elif n==4:
        print("Thank you for using the Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        continue

    print("\nDo you want to perform another operation? (yes/no)")
    again=input().lower()   
    if again=="no":
        print("Thank you for using the Student Management System. Goodbye!")
        break                    