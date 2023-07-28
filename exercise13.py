# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.

def fib_list(fib_length):
    fib = [1, 1]
    i = 1
    if fib_length == 0:
        return []
    elif fib_length == 1:
        return [1]
    else:
        while i < fib_length - 1:
            fib.append(fib[i - 1] + fib[i])
            i += 1
        return fib


fib_sequence = fib_list(int(input("Enter length for Fibonacci sequence: ")))
print(fib_sequence)
