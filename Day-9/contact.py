print("--------CONTACT BOOK--------")

def add_contacts():
    n=int(input("Enter number of contacts: "))
    for i in range(n):
        print("Enter name of contact: ",i+1)
        name=input()
        print("Enter phone number of contact: ",i+1)
        ph=input()
        print("Enter email of contact: ",i+1)
        email=input()
        with open("contacts.txt","a") as f:
            f.write(name+"\n")
            f.write(ph+"\n")
            f.write(email+"\n")
            f.write("\n")

def view_contacts():
    with open("contacts.txt","r") as f:
        w=f.readlines()
        for i in w:
            print(i.strip())    

def search_contacts():
    name = input("Enter name of contact: ")
    with open("contacts.txt", "r") as f:
        lines = f.readlines()
    found = False
    for i in range(len(lines)):
        if lines[i].strip() == name:

            print("\nContact Found:")
            print("Name:", lines[i].strip())
            print("Phone:", lines[i + 1].strip())
            print("Email:", lines[i + 2].strip())

            found = True
            break

    if not found:
        print("Contact not found.")

def delete_contacts():
    name = input("Enter the name of the contact you want to delete: ")
    with open("contacts.txt", "r") as f:
        lines = f.readlines()
    found = False
    for i in range(len(lines)):
        if lines[i].strip() == name:
            del lines[i:i+4]
            found = True
            break
    if found:
        with open("contacts.txt", "w") as f:
            f.writelines(lines)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")                

print("Welcome to Contact Book!")

while True:
    print("1.Add contacts")
    print("2.View contacts")
    print("3.Search contacts")
    print("4.Delete contacts")
    print("5.Exit")
    ans=int(input("Enter your choice: "))
    if ans==1:
        add_contacts()
    elif ans==2:
        view_contacts()
    elif ans==3:
        search_contacts()
    elif ans==4:
        delete_contacts()
    elif ans==5:
        break
    else:
        print("Invalid choice")
        continue
    print("Do you want to continue?[y/n]")
    ans=input()
    if ans=="n":
        break   
    else:
        continue
    