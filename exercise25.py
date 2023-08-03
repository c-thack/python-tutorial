# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#
# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.

correct = False
guesses = list(range(1, 101))
guess_count = 0
print("Think of a number from 1 to 100.")

while not correct:
    list_middle = int(len(guesses) / 2)
    guess = guesses[list_middle]
    guess_count += 1
    result = input("Is --" + str(guess) + "-- high, low, or right on? ")
    if result == "right on":
        correct = True
    elif result == "high":
        guesses = guesses[:list_middle]
    else:
        guesses = guesses[list_middle:]

print("It took " + str(guess_count) + " guesses to guess " + str(guess))
