round='y'
import random
while(round=='y'):
    number=random.randint(1,100)
    attempt=0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.\n")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        print("\nGreat! You have selected the Easy difficulty level.")
        print("Let's start the game!")
        while(attempt<=9):
            guess=int(input("Enter your guess: "))
            if(guess==number):
                print("Congratulations! You guessed the correct number in ",attempt," attempts.")
                break
            elif(guess>number):
                print("Incorrect! The number is less than", guess)
            else:
                print("Incorrect! The number is greater than", guess)
            attempt+=1

            
    elif(choice==2):
        print("\nGreat! You have selected the Medium difficulty level.")
        print("Let's start the game!")
        while(attempt<=4):
            guess=int(input("Enter your guess: "))
            if(guess==number):
                print("Congratulations! You guessed the correct number in ",attempt," attempts.")
                break
            elif(guess>number):
                print("Incorrect! The number is less than", guess)
            else:
                print("Incorrect! The number is greater than", guess)
            attempt+=1


    else:
        print("\nGreat! You have selected the Hard difficulty level.")
        print("Let's start the game!")
        while(attempt<=2):
            guess=int(input("Enter your guess: "))
            if(guess==number):
                print("Congratulations! You guessed the correct number in ",attempt," attempts.")
                break
            elif(guess>number):
                print("Incorrect! The number is less than", guess)
            else:
                print("Incorrect! The number is greater than", guess)
            attempt+=1
    if(attempt==10 or attempt==5 or attempt==3 ):

        print("You used all your chances! Better luck next time")
        print("The numbeer is ",number)
    round=input("Do you want to play again (y/n):")
