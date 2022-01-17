# Erik's Sample Python Game
# Created Jan 16th 2022

from random import randrange

def runGame():
    # Code to run game here
    print("Game is running")
    randomNum = (randrange(100))
    print("Random number is selected")
    counter = "apple" # Fun way to set a counter - number of letters in apple (5)

    for letters in counter: # Goes 5 times
        guess = input("What is your guess? (Remember between 1 and 100) : ")
        while guess.isnumeric() == False:
            guess = input("Your guess must be a number! : ")
        while int(guess) > 100:
            guess = input("Your guess must be a number between 1 and 100! Try Again : ")

        if (int(guess) == randomNum):
            print("You got it! You win! The random number was: " + str(randomNum))
            exit()
        elif(int(guess) > randomNum):
            print("Your guess is too high, guess lower!")
        else:
            print("Your guess is too low, Guess higher!")
    print("You have run out of guesses! The random number was: " + str(randomNum))
    print("Better luck next time! ")

def Greeting():
    print("Welcome to a Fun Python Guessing game")
    print("This game will select a random number between 1 - 100 and give you hints!")
    print("Please remember though!, You only get 5 guesses")
    letsPlay = input("Would you like to play - Yes or No? : ")
    while letsPlay.lower() != "yes" and letsPlay.lower() != "no": # Checks input
        letsPlay = input("You must enter either yes or no!, try again!:  ")
    return letsPlay

def GoodBye():
    print("Okay, Have a great day!")
    exit() # Exits the program

def PlayAgain():
    playAgain = input("Would you like to play again? :  - Yes or No? : ")
    while playAgain.lower() != "yes" and playAgain.lower() != "no":  # Checks input
        playAgain = input("You must enter either yes or no!, try again!:  ")
    return playAgain

def mainDriver():
    letsPlay = Greeting() # Greet the user
    if (letsPlay.lower() == "no"): # Checks if user wants to play
        GoodBye()
    runGame() # Runs the game
    playAgain = PlayAgain()
    if (playAgain.lower() == "yes"):
        runGame()
    print("Hope you had a good time, have a good rest of your day!")

mainDriver() # Run the program - Main
