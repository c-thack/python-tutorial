# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list
# minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
import random


def loop_remove_dups(check_list):
    no_dups = []
    for x in check_list:
        if x not in no_dups:
            no_dups.append(x)
    return no_dups


def set_remove_dups(check_list):
    return list(set(check_list))


a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 10]
# a = random.sample(range(50), 20)
print(loop_remove_dups(a))
print(set_remove_dups(a))
