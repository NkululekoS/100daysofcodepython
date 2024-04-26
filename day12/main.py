from art import logo
import random 


""""
A game of guessing any between 1 - 100, The user will get either 5 or 10 attempts depending on the level their chose. 
The user will be informed if the number is lower/higher than the correct number. 
"""


#generate a random number between 1 to 100. 
#choose the game level - input if the game is easy then set the chances/attempts to 10 and 5 - hard 
#choose a number between 1 - 100
#conditions for each number chosen, inform the user if the number is too low or too high


def set_level():
    game_level = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if game_level.lower() == "easy":
       attempts = 10
    elif game_level.lower() == "hard":
        attempts = 5
    return attempts

def main():
    print(logo)

    attempts = set_level()
    correct_number = random.randint(0,100)

    

    game_over = False
    
    while not game_over:

        print(f"Your have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess > correct_number:
            print("Too high.")
        elif guess < correct_number:
            print("Too low.")
        elif guess == correct_number:
            game_over = True
            print(f"You got it. The correct answer was {guess}.")

        attempts -= 1
        
        if attempts == 0:
            game_over = True
            print("You've ran out of guesses, you lose")
        elif not game_over:
            print("Guess again")



if __name__ == "__main__":
    main()




