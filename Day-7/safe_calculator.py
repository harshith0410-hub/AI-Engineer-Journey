print("---------Safe Calculator---------")

first_number=float(input("Enter the first number: "))
second_number=float(input("Enter the second number: "))
operation=input("Enter the operation (+, -, *, /): ")

if operation=="+":
    result=first_number+second_number
    print("The result is:", result)
elif operation=="-":
    result=first_number-second_number
    print("The result is:", result)
elif operation=="*":
    result=first_number*second_number
    print("The result is:", result)
elif operation=="/":
    try:
        result=first_number/second_number
        print("The result is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    finally:
        print("Division operation completed.")
else:
    print("Error: Invalid operation.")