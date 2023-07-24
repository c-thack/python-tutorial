who = "I"
what = "am cool"
print(who.lower() + "\n" + what.upper())
# backslash \ to print system used characters
# + to concatenate
print(what.upper().isupper())
print(len(what))  # length of string
print(what[3])  # pulls character from string (index starts at 0)
print(what.index("o"))  # shows index of first instance of the parameter
print(who + "\n" + what.replace("cool", "happy"))
