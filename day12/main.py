from art import logo
import random 

easy_level = 5
hard_level = 10

def set_level():
    game_level = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if game_level.lower() == "easy":
       return hard_level
    elif game_level.lower() == "hard":
        return easy_level

def main():

    print(logo)
    print("Welcome to the guessing number game.")
    print("I am thinking of a number between 1 and 100.")

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




