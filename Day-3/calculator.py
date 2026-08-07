print("--------Welcome to the Calculator Program----")
print("Available operations: +, -, *, /")
operator=input("Enter the operation you want to perform: ")

while True:
    if operator=="+":
        n=int(input("Enter the number of elements you want to add: "))
        for i in range(n):
            num=int(input("Enter number {}: ".format(i+1)))
            if i==0:
                result=num
            else:
                result+=num
        print("The result of addition is:", result)
        print("Do you want to perform another operation? (yes/no)")
        choice=input().lower()
        if choice=="yes":
            operator=input("Enter the operation you want to perform: ")
            continue
        else:
            print("Thank you for using the calculator. Goodbye!")
            break
    elif operator=="-":
        n=int(input("Enter the number of elements you want to subtract: "))
        for i in range(n):
            num=int(input("Enter number {}: ".format(i+1)))
            if i==0:
                result=num
            else:
                result-=num
        print("The result of subtraction is:", result)
        print("Do you want to perform another operation? (yes/no)")
        choice=input().lower()
        if choice=="yes":
            operator=input("Enter the operation you want to perform: ")
            continue
        else:
            print("Thank you for using the calculator. Goodbye!")
            break
    elif operator=="*":
        n=int(input("Enter the number of elements you want to multiply: "))
        for i in range(n):
            num=int(input("Enter number {}: ".format(i+1)))
            if i==0:
                result=num
            else:
                result*=num
        print("The result of multiplication is:", result)
        print("Do you want to perform another operation? (yes/no)")
        choice=input().lower()
        if choice=="yes":
            operator=input("Enter the operation you want to perform: ")
            continue
        else:
            print("Thank you for using the calculator. Goodbye!")
            break
    elif operator=="/":
        n=int(input("Enter the number of elements you want to divide: "))
        for i in range(n):
            num=int(input("Enter number {}: ".format(i+1)))
            if i==0:
                result=num
            else:
                if num==0:
                    print("Error: Division by zero is not allowed.")
                    break
                result/=num
        else:
            print("The result of division is:", result)
        print("Do you want to perform another operation? (yes/no)")
        choice=input().lower()
        if choice=="yes":
            operator=input("Enter the operation you want to perform: ")
            continue
        else:
            print("Thank you for using the calculator. Goodbye!")
            break
    else:
        print("Invalid operator. Please enter a valid operator (+, -, *, /).")
        operator=input("Enter the operation you want to perform: ")
