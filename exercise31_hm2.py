# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
# guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
# infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and
# display a different message if the player tries to guess that letter again. Remember to stop the game when all the
# letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of
# guesses the player has remaining - we will deal with those in a future exercise.


# prompts player to guess a letter
def guess_letter():
    return input("Guess a letter: ")


def update_progress(progress, word, last_guess):
    if last_guess in word:
        for i in range(len(word)):
            if word[i] == last_guess:
                progress[i] = last_guess
    else:
        print(f"Letter {last_guess} is not present.")


word_to_guess = 'evaporate'  # will randomize in later exercise
progress = list('_' * len(word_to_guess))  # initialize board with all blanks
guess = ''
guesses = []
guess_count = 0

print(''.join(progress))

while '_' in progress:  # loop while there's still a blank
    guess = guess_letter()
    if guess in guesses:
        print(f"Letter {guess} already guessed.")
        continue
    guesses.append(guess)
    guess_count += 1
    update_progress(progress, word_to_guess, guess)
    print(''.join(progress))

print(f"Finished in {guess_count} guesses!")
