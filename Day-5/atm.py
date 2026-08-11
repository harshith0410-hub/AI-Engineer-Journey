def balance_check(balance):
    print("Your current balance is:", balance)

def withdraw_money(balance):
    withdraw=int(input("Enter the amount you want to withdraw: "))
    if withdraw>balance:
        print("Insufficient balance.")
    else:
        balance-=withdraw
        print("Withdrawal successful. Your current balance is:", balance)
    return balance

def deposit_money(balance):
    deposit=int(input("Enter the amount you want to deposit: "))
    balance+=deposit
    print("Deposit successful. Your current balance is:", balance)
    return balance
    
print("---------Welcome to the ATM---------")
balance=10000
balance_check(balance)


while True:

    print("Choose an option you want to perform:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    n=int(input("Enter your choice: "))

    if n==1:
        balance_check(balance)

    elif n==2:
        balance=withdraw_money(balance)

    elif n==3:
        balance=deposit_money(balance)
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