friends = ["matt", "zach", "jake", "mike", "cameron"]  # can mix variable types in a list
print(friends)
print(friends[0])  # uses negatives to go backwards in the list, -1 is the last item
print(friends[1:4])  # can use '1:' to access everything from position 1 to the end; 1:4 goes TO 4, not through
friends[2] = "brent"
print(friends)
friends.append("matt")
print(friends)

# list functions - append (adds item to end of list), extend (adds a list to the end of the list),
# insert (adds item to list at specific index), remove (removes item from list), clear (removes everything in list),
# pop (removes last item in list), index (returns index of item in list), count (counts how many times an item is
# in the list), sort (sorts list in ascending order), reverse (reverses the list),
# copy (makes copy of list)

