# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a
# list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

def file_to_list(filename):  # cleaner with function
    return_list = []
    with open(filename, "r") as read_file:  # get in habit of using with
        line = read_file.readline()
        while line:
            return_list.append(int(line))
            line = read_file.readline()
    return return_list


# prime_file = open("primenums.txt", "r")
# happy_file = open("happynums.txt", "r")
#
# counter = 0
# prime_nums = prime_file.readlines()
# happy_nums = happy_file.readlines()
#
# for num in prime_nums:
#     prime_nums[counter] = int(num.strip())
#     counter += 1
#
# counter = 0
#
# for num in happy_nums:
#     happy_nums[counter] = int(num.strip())
#     counter += 1
prime_nums = file_to_list("primenums.txt")
happy_nums = file_to_list("happynums.txt")
overlap = [i for i in prime_nums if i in happy_nums]
print(overlap)

# prime_file.close()
# happy_file.close()
