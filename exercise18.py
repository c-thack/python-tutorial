# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a
# “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the
# correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the
# user at the end.

import random


def test_guess(user_guess, number_to_guess):
    cows_bulls = [0, 0]
    for i in range(len(number_to_guess)):  # iterate through the numbers as strings
        if user_guess[i] == number_to_guess[i]:
            cows_bulls[0] += 1
        else:
            cows_bulls[1] += 1
    return cows_bulls


number = str(random.randint(1000, 9999))
print(number)  # remove for actual "game"
guess_count = 0
winning = False

while not winning:
    guess = input("Enter a 4-digit number: ")  # can add input validation
    guess_count += 1
    cow_bull_count = test_guess(guess, number)
    print("Cows: " + str(cow_bull_count[0]) + ", Bulls: " + str(cow_bull_count[1]))
    if cow_bull_count[0] == 4:
        winning = True

print("Success! Number of guesses: " + str(guess_count))
