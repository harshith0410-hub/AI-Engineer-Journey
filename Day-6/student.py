class student:
    def __init__(self, name, age, branch, marks):
        self.name = name
        self.age = age
        self.branch = branch
        self.marks = []

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Branch: {self.branch}, Marks: {self.marks}")

    def add_mark(self, mark):
        self.marks.append(mark)

    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

s1 = student("Alice", 20, "Computer Science", [])
s1.add_mark(85)   
s1.add_mark(90)
s1.add_mark(78)
s1.display()
print(f"Average Marks: {s1.average_marks():.2f}")

s2 = student("Bob", 21, "Electrical Engineering", [])
s2.add_mark(88)
s2.add_mark(92)
s2.add_mark(80)
s2.display()
print(f"Average Marks: {s2.average_marks():.2f}")

s3 = student("Charlie", 22, "Mechanical Engineering", [])
s3.add_mark(75)
s3.add_mark(82)
s3.add_mark(89)
s3.display()
print(f"Average Marks: {s3.average_marks():.2f}")