# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print
# out the results to the screen. I have a .txt file for you, if you want to use it!
# Extra:
#
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count
# how many of each “category” of each image there are. This text file is actually a list of files corresponding to the
# SUN database scene recognition database, and lists the file directory hierarchy for the images.

read_file = open("names.txt", "r")
names = {}
line = read_file.readline().strip()

while line:
    if line in names:
        names[line] += 1
    else:
        names[line] = 1
    line = read_file.readline().strip()

print(names)

read_file.close()

# Extra section

read_file = open("sun.txt", "r")
categories = {}
line = read_file.readline()

while line:
    line = line.split("/")
    if line[2] in categories:
        categories[line[2]] += 1
    else:
        categories[line[2]] = 1
    line = read_file.readline()

print(categories)

read_file.close()
