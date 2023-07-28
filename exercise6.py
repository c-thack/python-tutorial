# Ask the user for a string and print out whether this string is a palindrome or not.  (only works with 1 word)

check = input("Enter a word: ")

if check == check[::-1]:
    print("palindrome")
else:
    print("not palindrome")
