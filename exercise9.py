# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right.
# Extras:
# # Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

number = random.randint(1, 9)
guess_count = 0

while True:
    guess = input("Enter a number from 1 to 9: ")
    guess_count += 1
    if guess == 'exit':
        break
    elif int(guess) == number:
        print("Success!")
        break
    elif int(guess) > number:
        print("Too big!")
    elif int(guess) < number:
        print("Too small!")

print(str(guess_count) + " attempt(s) were made.")
