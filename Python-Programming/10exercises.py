# funtion to find the maximum number
num = [2, 6, 8, 2, 5, 9]
num1 = [10, 19, 45, 78, 23, 56, 77, 97]


def maxNum(*args):
    max = 0
    for n in args:
        n > max
    print("Maximum Number:", n)


maxNum(*num)
maxNum(*num1)

# min() and max() method
# print(max(num))
# print(min(num))


# #funtion to find the minumum number
def minNum(*args):
    mini = min(args)
    print("Minimum Number:", mini)


minNum(*num)
minNum(*num1)

# Write a Python function to multiply all the numbers in a list.
print("\n Multiplication of numbers:")


def mult(*args):
    m = 1
    for n in args:
        m *= n
    return m


print(mult(*num))
print(mult(*num1))


# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(num):
    count = 1
    for n in range(1, num + 1):
        count *= n
    print("Factorial of {0} = {1}".format(num, count))


factorial(15)


# a function to check is a string is palindrome
def checkPalindrome(str):
    # reversedString = str[::-1].lower()
    reversedString = "".join(reversed(str)).lower()
    if reversedString == str.lower():
        return True
    return False


print(checkPalindrome("AzA"))
print(checkPalindrome("AZA"))
print(checkPalindrome("aZA"))
print(checkPalindrome("madam"))
print(checkPalindrome("enoLA"))


# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
def string_both_ends(str):
    if len(str) < 2:
        return "String has less than 2 characters"
    return str[:2] + str[-2:]


print(string_both_ends("w3resource"))
print(string_both_ends("w"))
