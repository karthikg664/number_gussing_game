import random

def greetings():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")


def level():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")
    
    while True:
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                lvl='Easy'
                chance=10
            elif choice==2:
                lvl='Medium'
                chance=5
            else:
                lvl='Hard'
                chance=3

            print(f"Great! You have selected the {lvl} difficulty level.")
            print("Let's start the game!\n")

            return chance
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")
        

def game(chance):
    num=random.randint(1,100)
    attempt=1
    while(attempt<chance):
            guess=int(input("Enter your guess: "))
            if(guess==num):
                print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
                break
            elif(guess>num):
                print(f"Incorrect! The number is less than {guess}")
            else:
                print(f"Incorrect! The number is greater than {guess}")
            attempt+=1
    if(attempt==chance ):
        print("You used all your chances! Better luck next time")
        print(f"The number is {num}")


if __name__=="__main__":
    turn='y'
    while(round=='y'):
        greetings()
        chance=level()
        game(chance)
        turn=input("Do you want to play again (y/n): ")
    