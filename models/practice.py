list2 = [1, 2, 3, 4, 5, 6, 9, 8, 8, 8]
my_tuple = (1, 2, 3, 4, 4, 5, 6, 8, 6)  # they are immutable
my_set = set(list2)  # they are unique and unorderd
print(sum(list2) / len(list2))

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print(set_one.difference(set_two))  # prints only elements that appear in in one of the sets
print(set_one.union(set_two))  # prints a unique combination of all the elements in the sets
print(set_one.intersection(set_two))  # prints all the elements that appear in both sets



name="kaseee"
for characters in name:
    print(characters)
print(name.count('e'))

if name.isupper():
    print("ndani")

