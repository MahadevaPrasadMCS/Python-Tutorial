# Rock - Paper - Scissor game using python.

import random

options = ["Rock","Paper","Scissor"]

def RPS():
    return 1

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
            print("Well played , that was fantastic game..")
            print(f"You got total {points} points..")
else:
    print("Oh, the computer system was waiting for you...!")
