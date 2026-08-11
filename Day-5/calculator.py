def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")

    choice = input("Enter operation: ")

    if choice == "+":
        result = add(a, b)

    elif choice == "-":
        result = subtract(a, b)

    elif choice == "*":
        result = multiply(a, b)

    elif choice == "/":
        result = divide(a, b)

    else:
        print("Invalid operation")
        continue

    print("Result:", result)

    again = input("\nDo you want to perform another operation? (yes/no): ").lower()

    if again == "no":
        print("Calculator closed.")
        break