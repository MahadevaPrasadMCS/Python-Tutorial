import random

words = [
    "laser", "motor", "drill", "cable", "gauge", "gear", "fluid", "plane", "optic", "force", "steel", "press", "clamp", "screw", "welds","engine", "design", "bridge", "circuit", "system", "sensor", "module", "robot", "driven",
    "thermal", "stress", "signal", "optics", "fluid", "power", "vector", "engineer", "dynamic", "digital",
    "control", "mechanics", "electrical", "software", "network", "structure", "process", "machine", "analysis",
    "prototype", "algorithm", "simulation", "technology", "hydraulic", "automation", "turbine", "semiconductor",
    "electronics", "mechanical", "engineering", "civil", "chemical", "environment", "transportation", "architecture",
    "instrument", "nanotechnology", "telecommunication", "microprocessor", "electromagnetics", "renewable",
    "thermodynamics", "aerodynamics", "computational", "robotics", "manufacturing", "cybersecurity", "bioengineering"
]


round_points = 0
secret_word = ""

def guess_word():
    global round_points
    global secret_word
    print("")
    diff_level = input("Select the level you of difficulty (easy or medium or hard): ").lower()
    print("")
    if diff_level == "easy":
        rand_len = random.randint(5,7)
        rand_words = [word for word in words if len(word) == rand_len and word != secret_word]
        points = 1
    elif diff_level == "medium":
        rand_len = random.randint(8,11)
        rand_words = [word for word in words if len(word) == rand_len and word != secret_word]
        points = 2
    elif diff_level == "hard":
        rand_len = random.randint(12,15)
        rand_words = [word for word in words if len(word) == rand_len and word != secret_word]
        points = 3
    else:
        print("You have not selected right option...")
        return
    
    secret_word = random.choice(rand_words)
    max_guess = 12
    
    print("")
    rand_list = list(secret_word)
    random.shuffle(rand_list)
    rand_word = "".join(rand_list)
    
    print("Ready to start the game...")
    print(f"Let's go, you selected {diff_level}")
    print(f"Your jumbled word \'{rand_word}\' , try to arrange in less guesses: ")
    print(f"You have {max_guess} guesses...")
    print("")
    i = 1
    guess = input(f"Start {i} guess : ").lower()
  
    
    while(True):
        if guess == secret_word:
            round_points += points
            if i == 1:
                print("Incredible! First try!")
                round_points += 2
            else:
                print("Wow , congratulations you guessed word correctly..")
            print(f"You are total points are  - {round_points} now..")
            print("")
            return round_points
        elif max_guess > 0:
            print("Oh , that is not correct..")
            print("")
            max_guess -= 1
            i += 1
            print(f"You have {max_guess} guesses...")
            guess = input(f"Start {i} guess : ").lower()
        else:
            print("")
            print(f"Sorry, you're out of guesses. The correct word was \'{secret_word}\'.")
            return round_points
     

print("----------------------------------------------------------")
print("")
print("________Welcome to word guessing game________")
print("")
print("Guess the scrambled word's correct version with minimum guess to earn more points...")
print("")

play = True

while play:
    print("----------------------------------------------------------")
    round_points = guess_word()
    print("")
    while True:
        continue_play = input("Play again? (yes/no): ").lower()
        if continue_play == "yes":
            break
        elif continue_play == "no":
            print("")
            print(f"Game over!, your total points {round_points} ")
            print("Great game! , come back to play more...")
            play = False
            break
        else:
            print("Sorry it was not a valid option...")
            print("--------------------------------------------------")
            continue
    
