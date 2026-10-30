# Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.


def guessing_game():

    number = int(input("Enter secret number (1-10): "))

    while True:
        guess = int(input("Guess a number (1-10): "))

        if guess == number:
            print("Congratulations! Correct guess.")
            break

        elif guess < number:
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

guessing_game()