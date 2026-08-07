import random
print("----------Welcome to Rock Paper Scissors Game----------" )
print("Enter Quit to exit the game.")
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice == "quit":
        print("Thanks for playing! Goodbye.")
        break
    elif user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    else:
        print(f"You chose: {user_choice}")
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

