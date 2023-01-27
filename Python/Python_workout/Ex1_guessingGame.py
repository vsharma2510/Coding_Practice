import random

def guessing_game():
    actualNumber = random.randint(0,100)
    inputNumber = 0
    while (actualNumber != inputNumber):
        try:
            inputNumber = int(input("Try to guess a number between 0 and 100 \n"))
        except ValueError:
            print("Please input a number!")
            continue
        if (actualNumber != inputNumber):
            print("Try again!")
            if (inputNumber < actualNumber):
                print("Go higher!")
            elif(inputNumber > actualNumber):
                print("Go lower!")
        if(actualNumber == inputNumber):
            print("You got it!")

guessing_game()