# can do exponents with '**' (2**3 == 8), this is just an exercise

def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result


print(raise_to_power(2, 3))
