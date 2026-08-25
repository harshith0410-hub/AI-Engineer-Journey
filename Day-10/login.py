import json     
print("-------LOGIN SYSTEM-------")

def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def register_user():
    users = load_users()
    name = input("Name: ")
    password = input("Password: ")
    if name in users:
        print("User already exists.")
        return
    
    users.append({
        "name": name,
        "password": password
    })
    save_users(users)
    print("User registered!")

def login():
    users = load_users()
    name = input("Name: ")
    for user in users:
       
        if user["name"].lower() == name.lower():
            print("User already exists.")
            return

def view_users():
    users = load_users()
    if not users:
        print("No users found.")
        return
    for user in users:
        print(f"Name: {user['name']}")
        print("-"*20)

while True:
    print("\n1. Register User")
    print("2. Login")
    print("3. View Users")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login()
    elif choice == "3":
        view_users()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

