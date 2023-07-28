# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
# user the same string, except with the words in backwards order.

# def word_list(input_string):  # don't really need to function this...
#     return input_string.split(" ")

def reversal(input_string):  # probably the worst way to do this...
    words = input_string.split(" ")
    new_string = ""
    i = -1
    while abs(i) <= len(words):
        new_string = new_string + words[i] + " "
        i -= 1
    return new_string
# could also use .reverse then .join or the [::-1] thing


def reversal2(input_string):
    return " ".join(input_string.split()[::-1])


reverse_this = input("Reverse this string: ")
print(reversal(reverse_this))
print(reversal2(reverse_this))
