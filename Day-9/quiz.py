print("----------WELCOME TO QUIZ--------")

questions={
    "Which symbol is used to assign a value to a variable in Python?":["==","=",":","=>"],
    "Which of the following is a Python list?":["(1,2,3,)","{1,2,3}","[1,2,3]","<1,2,3,>"],
    "Which keyword is used to define a function in Python?":["function","defun","func","def"],
    "Which mode is used to append data to an existing file?":["r","w","a","s"],
    "Which method is automatically called when an object is created?":["__start()","__init__","__new__","__init_subclass__"],
}

answers=["b","c","d","c","b"]

def quiz(questions,answers):
    score=0
    for i, (question, options) in enumerate(questions.items()):
        print(f"\nQuestion {i+1}: {question}")

        for j, option in enumerate(options):
            print(f"{chr(65+j)}. {option}")

        ans = input("Enter your answer: ").lower()

        if ans == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("The correct answer is:", answers[i])
    print(f"Your score is {score}/{len(questions)}")
    print("Do you want to play again?[y/n]")
    ans=input()
    if ans=="y":
        quiz(questions,answers)
    else:
        print("Thank you for playing!")

quiz(questions,answers)