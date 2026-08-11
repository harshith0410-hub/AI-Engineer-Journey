print("---------Welcome to the ATM---------")
balance=10000
print("Your current balance is:", balance)


while True:

    print("Choose an option you want to perform:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    n=int(input("Enter your choice: "))

    if n==1:
        print("Your current balance is:", balance)

    elif n==2:
        withdraw=int(input("Enter the amount you want to withdraw: "))
        if withdraw>balance:
            print("Insufficient balance.")
        else:
            balance-=withdraw
            print("Withdrawal successful. Your current balance is:", balance)

    elif n==3:
        deposit=int(input("Enter the amount you want to deposit: "))
        balance+=deposit
        print("Deposit successful. Your current balance is:", balance)

    elif n==4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    print("\nDo you want to perform another operation? (yes/no)")
    again=input().lower()
    if again=="no":
        print("Thank you for using the ATM. Goodbye!")
        break                    