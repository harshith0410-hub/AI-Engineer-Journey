import json

def load_expenses():
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    expenses = load_expenses()

    name = input("Name: ")
    amount = float(input("Amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    save_expenses(expenses)
    print("Expense added!")            

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for e in expenses:
        print(f"Name: {e['name']}")
        print(f"Amount: {e['amount']}")
        print("-"*20)

def search_expense():
    expenses = load_expenses()
    name = input("Enter name: ")

    for e in expenses:
        if e["name"].lower() == name.lower():
            print("Expense Found!")
            print(f"Item: {e['name']}")
            print(f"Amount: ${e['amount']}")
            return

    print("Expense not found.")

def total_expenses():
    expenses = load_expenses()
    total = 0

    for e in expenses:
        total += e["amount"]

    print(f"Total expenses: ${total}")

def highest_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    highest = max(expenses, key=lambda e: e["amount"])

    print(f"Highest Expense: {highest['name']}")
    print(f"Amount: ₹{highest['amount']}")


def delete_expense():
    expenses = load_expenses()
    name = input("Enter name to delete: ")

    for e in expenses:
        if e["name"].lower() == name.lower():
            expenses.remove(e)
            save_expenses(expenses)
            print("Deleted.")
            return

    print("Expense not found.")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Total Expenses")
    print("5. Highest Expense")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        total_expenses()
    elif choice == "5":
        highest_expense()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

