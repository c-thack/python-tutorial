is_male = False

# can put or/and in condition or comparison operators (==, !=, <, >, <=, >=)
if is_male:
    # code needs to be indented
    print("you are male")
else:  # use 'elif' to do else if (new condition)
    print("you are not male")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    else:
        return num3


print(max_num(1, 4, 7))
