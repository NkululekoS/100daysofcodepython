from art import logo
import random 

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
   
        if attempts == 0:
            game_over = True
            print("You've ran out of guesses, you lose")
        elif not game_over:
            attempts -= 1
            print("Guess again")

if __name__ == "__main__":
    main()




