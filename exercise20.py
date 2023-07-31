# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.


def search(ordered_list, number):
    for num in ordered_list:
        if num == number:
            return True
    return False


def binary_search(ordered_list, number):
    while len(ordered_list) > 1:
        list_middle = int(len(ordered_list) / 2)
        if number < ordered_list[list_middle]:
            ordered_list = ordered_list[:list_middle]
        else:
            ordered_list = ordered_list[list_middle:]
    return ordered_list[0] == number


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = int(input("Find this number in list 'a': "))

print(search(a, b))
print(binary_search(a, b))
