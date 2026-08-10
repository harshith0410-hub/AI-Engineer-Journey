print("--------Welcome to the Student Management System--------")
n=["name","age","branch","marks","CGPA"]
dic={}
for i in n:   
    dic[i]=input(f"Enter your {i}: ")
print("--------Student Details--------")
for key, value in dic.items():
    print(f"{key}: {value}")    
print("Do you want to update any details? (yes/no)") 
if input().lower()=="yes":
    print("Which detail do you want to update? (name/age/branch/marks/CGPA)")
    key=input()
    if key in dic:
        dic[key]=input(f"Enter your new {key}: ")
        print(f"{key} updated successfully.")
    else:
        print("Invalid detail.")

print("--------Updated Student Details--------")           
for key, value in dic.items():
    print(f"{key}: {value}")    

print("Do you want to delete any details? (yes/no)")
if input().lower()=="yes":
    print("Which detail do you want to delete? (name/age/branch/marks/CGPA)")
    key=input()
    if key in dic:
        del dic[key]
        print(f"{key} deleted successfully.")
    else:
        print("Invalid detail.")

print("--------Final Student Details--------")
for key, value in dic.items():
    print(f"{key}: {value}")