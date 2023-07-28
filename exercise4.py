# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a
# divisor of 26 because 26 / 13 has no remainder.)

num1 = int(input("Enter a number: "))
check = range(2, num1+1)
print(check)
print(str(num1) + " is divisible by: ")
for x in check:
    if num1 % x == 0:
        print(x)  # or make/append to a new list and print it at the end

