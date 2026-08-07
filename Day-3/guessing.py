import random
n=random.randint(1,100)
i=int(input("Guess a number between 1 and 100: "))
count=1
while True:
    if i<n:
        print("Your guess is too low. Try again.")
        i=int(input("Guess a number between 1 and 100: "))
        count += 1  
    elif i>n:
        print("Your guess is too high. Try again.")
        i=int(input("Guess a number between 1 and 100: "))
        count += 1
    else:
        print("Congratulations! You guessed the correct number:", n)
        print("It took you", count, "guesses.")
        break
