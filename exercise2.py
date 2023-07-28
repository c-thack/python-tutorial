# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
# to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num1 = int(input("Enter a number: "))

if num1 % 4 == 0:
    print(str(num1) + " is even and divisible by 4!")
elif num1 % 2 == 0:
    print(str(num1) + " is even!")
else:
    print(str(num1) + " is odd!")

num1 = int(input("Enter a number: "))
check = int(input("Divide that by: "))

if num1 % check == 0:
    print(str(num1) + " is divisible by " + str(check))
else:
    print(str(num1) + " is not divisible by " + str(check))

