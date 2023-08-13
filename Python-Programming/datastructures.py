# Data Structures are designed to work with more complex information, such as a collection of data like a list of people or a list of companies

# Data structures in python are divided into:
# Built-in Data Structures:
# List, Tuples, Sets, Dictionary

# User-Defined Data Structures:
# Stack, Tree, Graph, Queue, Linked List, HashMap

# A data structure allows you to organize and arrange your data to perform operations on them. Python has the following built-in data structures: List, dictionary, tuple and set. These are all considered non-primitive data structures, meaning they are classed as objects, this will be explored later in the course.

# LISTS

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C"]
list3 = ["Hello", 1, True, 40.50]

list4 = [1, [2, 3, 4], 5, 6]  # nested list

# print an element at a specified index
print(list1[2])

# insert(): insert elements to the list at a specified index
list1.insert(len(list1), 6)
print(list1)

# append(): simply append element to the list
list1.append(7)
print(list1)

# extend(): extends the list by adding elements (list) to it
list2.extend(["D", "E", "F"])
print(list2)

# pop(): removes the last element from the list
list3.pop()
print(list3)

# del(): deletes an element from the list at a specified index
del list4[1]
print(list4)

# iterate a list
for i in list2:
    print("Letter: ", i)


# TUPLES
# tuples are like list, but they are immutable

myTuples = (1, "Hello", 0.5, True)
print(myTuples.count("Hello"))
print(myTuples.index("Hello"))
print(myTuples.index(True))  # will output 0 because 1 is true

for x in myTuples:
    print("X:", x)


# SETS
set1 = {1, 1, 2, 3, 4}
print("set1:", set1)

# add an element into a set
set1.add(5)
print("set1:", set1)

# remove an element from a set
set1.discard(5)
print("set1: ", set1)

# perform union of sets
set2 = {3, 4, 6, 6, 7, 8, 8, 9}
set3 = set1.union(set2)  # set3 = set1 | set2
print("set3:", set3)

# perform intersection of sets
set3 = set1.intersection(set2)  # set3 = set1 & set2
print("set3:", set3)

# perform difference of sets
set3 = set1.difference(set2)
print("set3:", set3)  # set3 = set1 - set2

# perform symmetric difference of sets
set3 = set1.symmetric_difference(set2)
print("set3:", set3)  # set3 = set1 ^ set2

for st in set3:
    print("Set:", st)


# DICTIONARY
dict1 = {1: "One", 2: "Two", 3: "Three", 4: "$four"}

# print the value of the said key
print(dict1[1])

# update a dictionary using it key
dict1[4] = "Four"
print(dict1)

# add a new key and value to a dict
dict1[5] = "Five"
print(dict1)

# add a new key and value to a dict and remove it
dict1[6] = "Six"
print(dict1)
dict1.pop(6)  # remove a key-value from a dict
print(dict1)

# iterate through a dict and print keys and values
for key, value in dict1.items():
    print("{0} + {1}".format(key, value))

# iterate and print keys only
for key in dict1.keys():
    print("Key:", key)

# iterate and print values only
for value in dict1.values():
    print("Values:", value)
