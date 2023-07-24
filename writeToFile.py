file = open("readfromme.txt", "a")  # using "w" overwrites everything the file, "a" appends to end
file.write("yes, yes it is")
file.close()

file2 = open("newfile.txt", "w")  # makes new file if it doesn't exist
file2.write("look at this new stuff")
file2.close()
