# have to open file before reading it; modes r = read, w = write, a = append, r+=read+write
read_file = open("readfromme.txt", "r")

# print(read_file.readline())  # moves the cursor
# print(read_file.readline())
# print(read_file.readlines()[1])  # reads specific line, but still goes based on where the cursor is
for line in read_file.readlines():
    print(line)
# make sure to close the file
read_file.close()
