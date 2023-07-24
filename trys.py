try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError as err:  # can save the error into a variable
    print(err)
except ZeroDivisionError:  # don't use bare excepts, catch specific errors
    print("Divided by zero")

