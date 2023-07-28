# exercise5 but using list comprehensions

import random

a = random.sample(range(50), 20)
b = random.sample(range(50), 25)

c = [i for i in a if i in b]  # and i not in c ? >>> can't easily check for duplicates without using sets

print(set(c))  # use set(c) to remove duplicates
