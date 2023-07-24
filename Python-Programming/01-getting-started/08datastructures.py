#Data Structures are designed to work with more complex information, such as a collection of data like a list of people or a list of companies

#Data structures in python are divided into:
    #Built-in Data Structures:
        #List, Tuples, Sets, Dictionary

    #User-Defined Data Structures:
        #Stack, Tree, Graph, Queue, Linked List, HashMap

#A data structure allows you to organize and arrange your data to perform operations on them. Python has the following built-in data structures: List, dictionary, tuple and set. These are all considered non-primitive data structures, meaning they are classed as objects, this will be explored later in the course. 

#LISTS

list1 = [1,2,3,4,5]
list2 = ["A", "B", "C"]
list3 = ["Hello", 1, True, 40.50]

list4 = [1, [2,3,4], 5, 6] #nested list

#print an element at a specified index
print(list1[2]) 

#insert(): insert elements to the list at a specified index
list1.insert(len(list1), 6)
print(list1)

#append(): simply append element to the list
list1.append(7)
print(list1)

#extend(): extends the list by adding elements (list) to it
list2.extend(["D", "E", "F"])
print(list2)

#pop(): removes the last element from the list
list3.pop()
print(list3)

#del(): deletes an element from the list at a specified index 
del list4[1]
print(list4)

#iterate a list
for i in list2:
    print("Letter: ", i)


#TUPLES
#tuples are like list, but they are immutable

myTuples = (1, "Hello", 0.5, True)
print(myTuples.count("Hello"))
print(myTuples.index("Hello"))
print(myTuples.index(True)) #will output 0 because 1 is true

for x in myTuples:
    print("X:", x)


#SETS