# Rock - Paper - Scissor game using python.

import random

options = ["Rock","Paper","Scissor"]

def RPS():
    print()
    print("So bold of you, defeat the system")
    print()
    userPoints = 0
    nextRound = "go"
    
    while nextRound == "go":
        systemChoice = random.choice(options).lower()
        userChoice = input("Enter your option(Rock-Paper-Scissor) : ").lower()
        print()
        print(f"Your choice : {userChoice}")
        print(f"System choice : {systemChoice}")
        
        if userChoice == systemChoice:
            print("Aha, you both chose the same option")
        elif userChoice == "rock":
            if systemChoice == "scissor":
                print("You defeated the system")
                userPoints += 1
            else:
                print("System defeated you")
        elif userChoice == "scissor":
            if systemchoice == "paper":
                print("You defeated the system")
                userPoints += 1
            else:
                print("System defeated you")
        else:
            if systemChoice == "rock":
                print("You defeated the system")
                userPoints += 1
            else:
                print("System defeated you")
        print()
        nextRound = input("Let's play another round (go or stop): ").lower()
    return userPoints

print("==========================================================")
print("Welcome to the classical Rock - Paper - Scissor game")
print()
print("Try to make more points than computer...")
print("==========================================================")
print()

start = input("Let's start the game(yes or no): ").lower()

if start == 'yes':
    while True:
        points = RPS()
        choice = input("Wow that was a good game with you, let's continue(yes or no): ").lower()
        if choice == "yes":
            continue
        else:
            print("Well played , that was a fantastic game..")
            print()
            print(f"You got total {points} points..")
            break
else:
    print("Oh,computer system was waiting for you...!")
