print("---------Welcome to the Contact Management System---------")

n=int(input("Enter the number of contacts you want to add: "))
contacts={}

for i in range(n):
    name=input("Enter contact name: ")
    phone=input("Enter contact phone number: ")
    email=input("Enter contact email address: ")
    contacts[name]={"phone": phone, "email": email}
    
print("---------Contact Details---------")
for name, details in contacts.items():
    print(f"Name: {name}")
    print(f"Phone: {details['phone']}")
    print(f"Email: {details['email']}")
    print()

while True:
    print("Do you want to search, update, or delete a contact? (search/update/delete/exit)")
    action=input().lower()
    if action=="search":
        name=input("Enter the contact name to search: ")
        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
            continue
        else:
            print("Contact not found.")
            continue
    elif action=="update":
        name=input("Enter the contact name to update: ")
        if name in contacts:
            phone=input("Enter new phone number: ")
            email=input("Enter new email address: ")
            contacts[name]={"phone": phone, "email": email}
            print("Contact updated successfully.")
            continue
        else:
            print("Contact not found.")
            continue
    elif action=="delete":
        name=input("Enter the contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
            continue
        else:
            print("Contact not found.")
            continue
    elif action=="exit":
        break
    else:
        print("Invalid action. Please choose search, update, delete, or exit.")
        continue                            

print("---------Final Contact Details---------")
for name, details in contacts.items():
    print(f"Name: {name}")
    print(f"Phone: {details['phone']}")
    print(f"Email: {details['email']}")
    print()    