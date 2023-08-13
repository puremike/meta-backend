import time

"""WRITING ALGORITHMS

An algorithm is a set of instructions that is completed in a step-by-step way to solve a particular problem.

There are many different types of algorithms that have been designed to solve all kinds of different types of problems in computer science. When writing an algorithm, it can be solved in many different ways and each can have its own pros and cons.

Recursion
Recursion refers to a method or a function that will call itself. It is used to resolve problems by breaking the problem down into sub-problems. Let us take a look at some of the most popular types of recursive algorithms.

Divide and conquer
This consists of two parts. The first is breaking the problem down into smaller sub-problems and the second is solving the final solution.

Dynamic programming
This is mainly used for optimization problems. It is similar to the divide and conquer algorithm in that it splits the problems into sub-problems.

Greedy algorithm
This one finds the best solution in each and every step instead of approaching optimization in a global way."""


"""MAKE A COFFEE - SOLUTION

Input
Ingredients required:

Cup
Hot water
Coffee granules

Optional:
Milk
Cream
Sugar

Output
A cup of coffee.

Steps
1. Add drinking water to an electric kettle.
2. Put the kettle on to boil water.
3. While waiting, prepare coffee.
4. Add coffee granules to the cup.
5. If water is boiled, pour water into a cup, else continue to wait.
6. If milk or cream is required, add and stir
7. If sugar is required, add and stir.
8. Return coffee.
"""

# ALGORITHMIC COMPLEXITY
# Refactoring is a standard part of the software development cycle. Making code easier to manage, maybe straightforward, but what about making it faster or making it perform better? To determine how to make code faster or perform better, you must be able to measure it. Code is measured by TIME and SPACE. TIME is measured by how long it takes and SPACE is about how much memory it uses.

#  Let's explore the different kinds of time complexities:

# 1, CONSTANT TIME - This is an algorithm that will always run under the same time and space regardless of the size

drinks = {1: "Coffee", 2: "Tea", 3: "Juice"}
print(drinks[2], "\n")  # output = Tea; iteration = 0, so the time is constant


# 2, LINEAR TIME -  This will grow depending on the size of the input. For example, if I have an array of numbers with a range of 100, it will run very fast. But if it's increased to a million, it will take a lot longer to complete. The SIZE in this case, affects the RUNNING TIME of the code.

# the bigger the range, the bigger the running time

for x in range(100):
    print(x, end=" ")

# but if the range is 1000000, it will take more time to execute program- LINEAR TIME


#  3, LOGARITHMIC TIME algorithm refers to the running time of the inputs against the number of operations. I can take a linear approach to try to find a number out of 100. Let's say the number is 97. In a linear equation, it will take 96 iterations before it's found. This is because it must iterate through each item one by one until it finds the target value.

print("\n")


def findNum(n):
    count = 0
    for x in range(1, 1000):
        if x == n:
            print("Total Iterations:", count)
            return x
        count += 1


findNum(179)  # 178 iterations

# Using a binary search, I can drastically cut down the iterations and find it on the seven iterations. This is measured by logarithmic time. The binary search works by splitting the list into two parts each time to check if a target is less than or greater than one.


def findNumberLog(target):
    iterations = 0
    x = range(100)
    left = 0
    right = len(x) - 1

    while left <= right:
        iterations += 1
        middle = left + right  # 2
        isNumber = x[middle]

        if target == isNumber:
            print("Iterations:", iterations)
            return middle
        elif target < isNumber:
            right = middle - 1
        else:
            left = middle + 1
    return -1


print(findNumberLog(97))


# 4, QUADRATIC TIME refers to a linear operation of each value of the input data squared. This is often a nested list, as in this for loop. This for loop is considered quadratic time as the outer loop will need to iterate in a linear way 10 times.

for x in range(10):
    for y in range(10):
        print(x, y, end=" ")
# it means the total iterations for the for loops is 10 * 10 = 100

"""
5, EXPONENTIAL TIME, which is an algorithm that doubles with each iteration. The Fibonacci sequence is a prime example of this.

def fibonacci(n):
     if n < 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)"""


"""BIG-0 NOTATION
Big-O notation is the most fundamental tool to measure the cost of an algorithm. It describes the complexity of the code using algebraic terms.
Function        Big O Notation
Constant        O(c)
Logarithmic     O(log(n))
Linear          O(n)
Quadratic       O(n^2)
Cubic           O(n^3)
Exponential     O(2^n)
Factorial       O(n!)"""
