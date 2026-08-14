class account:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance

    def check_balance(self):
        print("Your current balance is:", self.balance)

    def withdraw_money(self):
        withdraw=int(input("Enter the amount you want to withdraw: "))
        if withdraw>self.balance:
            print("Insufficient balance.")
        else:
            self.balance-=withdraw
            print("Withdrawal successful. Your current balance is:", self.balance)

    def deposit_money(self):
        deposit=int(input("Enter the amount you want to deposit: "))
        self.balance+=deposit
        print("Deposit successful. Your current balance is:", self.balance)

while True:

    print("---------Welcome to the Bank Account---------")
    name=input("Enter your name: ")
    acc_no=input("Enter your account number: ")
    balance=int(input("Enter your initial balance: "))

    user=account(name,acc_no,balance)

    while True:
        print("\nChoose an option you want to perform:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        n=int(input("Enter your choice: "))

        if n==1:
            user.check_balance()

        elif n==2:
            user.withdraw_money()

        elif n==3:
            user.deposit_money()
        elif n==4:
            print("Thank you for using the Bank Account. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    print("\nDo you want to perform another operation? (yes/no)")
    again=input().lower()
    if again=="no":
        print("Thank you for using the Bank Account. Goodbye!")
        break                        