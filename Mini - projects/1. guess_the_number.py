import random

def guess_number():
    num = random.randint(1,100)
    
    print("----- Welcome To guess a number game -----")
    print("")
    print("Guess the number between 0 - 100 as early as possible...")
    print("")
    print("--------------------------------------------------------")
    
    print("")
    difficulty = input("Choose your difficulty level(easy / medium / difficult): ").lower()
    if difficulty == "easy":
        print("You selected easy level..")
        print("")
        max_guess = 20
    elif difficulty == "difficult":
        print("You selected easy level..")
        print("")
        max_guess = 10
    elif difficulty == "medium":
        print("You selected easy level..")
        print("")
        max_guess = 15
    else:
        return "Please select a valid level"
    
    
    i = 1
    while max_guess > 0 :
        try:
            guess = int(input(f"Enter your {i} guess: "))
        except ValueError:
            print("Please enter only an integer value")
            print("")
            continue
            
        if(guess > num):
            print("Ohh you guessed too high number")
            i += 1
            max_guess -= 1
            print(f"You have {max_guess} chance left")
            print("")
        elif(guess < num):
            print(f"Ohh you guessed too low number")
            i +=1
            max_guess -= 1
            print(f"You have {max_guess} chance left")
            print("")
        else:
            return f"Wow, Congratulations you guessed the right number in {i} tries..."
            break
    return f"Sorry , your chances are over, the correct number was {num} try again..."

while True:
    print(guess_number())
    play_again = input("Want to play again (yes or no): ").lower()
    if play_again != "yes":
        print("meet you again sometimes...")
        break
    print("")
    


        
