# Ask the user for a number and determine whether the number is prime or not.
def get_divisors(number):
    check = range(2, round(number/2) + 1)
    divisors = [x for x in check if number % x == 0]
    # for x in check:
    #     if number % x == 0:
    #         divisors.append(x)
    return divisors


num1 = int(input("Enter a number: "))
if len(get_divisors(num1)) == 0:
    print(str(num1) + " is prime!")
else:
    print(str(num1) + " is not prime!")
