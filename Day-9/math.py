import utils

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

while True:
    print("Choose operation from given menu")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Square")
    print("7.Cube")
    print("8.Exit")
    
    op=int(input("Enter your option: "))
    if op==1:
        c=utils.add(a,b)
        print("Sum is: ",c)
    elif op==2:
        c=utils.subtract(a,b)
        print("Difference is: ",c)
    elif op==3:
        c=utils.multiply(a,b)
        print("Product is: ",c)
    elif op==4:
        c=utils.divide(a,b)
        print("Quotient is: ",c)
    elif op==5:
        c=utils.power(a,b)
        print("Power is: ",c)
    elif op==6:
        c=utils.square(a)
        print("Square is: ",c)
    elif op==7:
        c=utils.cube(a)
        print("Cube is: ",c)
    elif op==8:
        break
    else:
        print("Invalid option") 
        continue
    print("Do you want to continue?[y/n]")
    ans=input()
    if ans=="n":
        break   
    else:
        continue