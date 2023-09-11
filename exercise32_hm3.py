#  Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
#
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them -
# let them guess again.
# Optional additions:
#
# When the player wins or loses, let them start a new game. (done)
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. (zzz)

import random


# choose a random word from the sowpods list
def pick_word(filename):
    with open(filename, 'r') as words:
        word_list = list(words)
    return word_list[random.randrange(len(word_list))].strip().lower()


# update the display
def update_progress(progress, word, last_guess, count):
    if last_guess in word:
        for i in range(len(word)):
            if word[i] == last_guess:
                progress[i] = last_guess
        return 0
    else:
        print(f"Letter {last_guess} is not present.  {5 - count} mistakes left.")
        return 1


# main gameplay loop
def game_loop():
    word_to_guess = pick_word("sowpods.txt")
    progress = list('_' * len(word_to_guess))  # initialize board with all blanks
    guesses = []
    guess_count = 0
    mistakes = 0

    print(''.join(progress))

    while '_' in progress and mistakes < 6:  # loop while there's still a blank
        guess = input("Guess a letter: ")
        if guess in guesses:
            print(f"Letter {guess} already guessed.")
            continue
        guesses.append(guess)
        guess_count += 1
        mistakes += update_progress(progress, word_to_guess, guess, mistakes)
        print(''.join(progress))

    if mistakes == 6:
        print(f"Too many mistakes!  The word was {word_to_guess}.")
    else:
        print(f"Finished in {guess_count} guesses and {mistakes} mistakes!")


# replay code
play = True

while play:
    game_loop()
    if input("Play again? y or n: ") == 'n':
        play = False
