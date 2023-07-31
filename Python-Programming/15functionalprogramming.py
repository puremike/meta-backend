#  Functions take some input, process it and then produce some outputs. There are two types of functions, namely - TRADITIONAL and PURE
# Pure functions will always do the same thing and return the same results no matter how many times they are called.

# Traditional functions can access and modify variables on the global state, but pure functions cannot, both traditional functions and pure functions can access variables in the local state. Traditional functions can change our dogs, whereas pure functions cannot, and lastly, the outputs of traditional functions does not depend on inputs. However, the output of pure functions does depend on input, functional programming in essence is a programming paradigm that utilizes functions for clean, consistent and maintainable code.

# IMPURE FUNCTION

# global variable
my_list = [1, 2, 3, 4]


def add_to_list(item):
    return my_list.extend(item)


add_to_list([5, 6, 7, 8, 9, 10])
print("Impure function:", my_list)
# the above function is !pure function because it has altered the global variable


# now we'll twerk the above traditional (impure) function to a pure function

# PURE FUNCTION
my_list2 = [1, 2, 3, 4]


def add_to_ls(list, item):
    nl = list.copy()
    nl.extend(item)
    return nl


new_list = add_to_ls(my_list2, [5, 6, 7, 8, 9])
print("Pure function:", new_list)

# RECURSION - recursing is a function that calls itself
# Disadvantages of recursion: It can be hard to follow the logic of the code; it can be difficult to debug; memory is expensives
print("\n")
# using a function that returns a factorial(n)


def find_factorial_recursive(n):
    if n < 0:
        return "Enter a positive number:)"
    elif n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)


print("Factorial:", find_factorial_recursive(5))


print("\n")
# function to reverse a string:
string_a = ["Mike", "Madam", "Goal", "Racecar"]


def reverse_string(list):
    for str in list:
        reversed_string = str[::-1]
        print(reversed_string)


reverse_string(string_a)

# Function for checking a palindrome
print("\n")


string_b = ["AKa", "HaaH", "leVEL", "roToR", "maDAM"]


def check_palindrome(list):
    for str in list:
        # reversed_string = str[::-1]
        reversed_string = "".join(reversed(str)).lower()
        if str.lower() == reversed_string:
            print(str, "is a palindrome!!")
        else:
            print(str, "is not a palindrome!!")


check_palindrome(string_a)

print("\n")
check_palindrome(string_b)


# MAP & FILTER
# It's used to map and filter through a list

print("\n")
menu = ["espresso", "mocha", "latte", "cappucino", "cortado", "americano"]


def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee


# using map() - returns all the iterables in the list
mapped_coffee = map(find_coffee, menu)
print(mapped_coffee)
for x in mapped_coffee:
    print(x)

print("\n")

# using filter() - print interables that are true
for x in filter(find_coffee, menu):
    print(x)


print("\n")

# EXAMPLES
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x * 2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)
