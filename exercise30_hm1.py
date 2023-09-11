# This exercise is Part 1 of 3 of the Hangman exercise series.
# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS
# dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s
# compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a
# single word.

import random


def pick_word(filename):
    with open(filename, 'r') as words:
        word_list = list(words)
    return word_list[random.randrange(len(word_list))].strip()


print(pick_word("sowpods.txt"))
