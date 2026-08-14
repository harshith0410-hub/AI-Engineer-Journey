class car:
    def __init__(self,brand,model,year,price):
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price

    def display(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)
        print("Car Year:", self.year)
        print("Car Price:", self.price)

    def start(self):
        print(f"The {self.brand} {self.model} is starting.")

    def stop(self):
        print(f"The {self.brand} {self.model} is stopping.")

print("---------Car Information---------")
cars=[]
for i in range(3):
    brand=input("Enter the car brand: ")
    model=input("Enter the car model: ")
    year=int(input("Enter the car year: "))
    price=float(input("Enter the car price: "))
    cars.append(car(brand,model,year,price))

while True:
    print("\nChoose an option you want to perform:")
    print("1. Display Car Information")
    print("2. Start Car")
    print("3. Stop Car")
    print("4. Exit")

    n=int(input("Enter your choice: "))

    if n==1:
        print("Which car's information do you want to display? (1, 2, or 3)")
        car_choice=int(input("Enter your choice: "))
        if car_choice in [1, 2, 3]:
            cars[car_choice-1].display()
        else:
            print("Invalid choice. Please try again.")
    elif n==2:
        print("Which car do you want to start? (1, 2, or 3)")
        car_choice=int(input("Enter your choice: "))
        if car_choice in [1, 2, 3]:
            cars[car_choice-1].start()
        else:
            print("Invalid choice. Please try again.")
    elif n==3:
        print("Which car do you want to stop? (1, 2, or 3)")
        car_choice=int(input("Enter your choice: "))
        if car_choice in [1, 2, 3]:
            cars[car_choice-1].stop()
        else:
            print("Invalid choice. Please try again.")
    elif n==4:
        print("Thank you for using the Car Information System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    print("\nDo you want to perform another operation? (yes/no)")
    again=input().lower()
    if again=="no":
        print("Thank you for using the Car Information System. Goodbye!")
        break    


                  