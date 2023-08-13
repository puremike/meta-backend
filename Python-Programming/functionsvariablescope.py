# We have four scopes in Python:
# Local Scope: variables are accessible within a function only

# Enclosing Scope: Enclosing scope refers to a function inside another function or what is commonly called a nested function.

# Global Scope: Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere.

# Built-in Scope: Built-in scope refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth.  Functions with built-in scope can be accessed at any level.

# All these scopes are regarded as LEGB

# global scope
myGlobal = 10


def fn1():
    # local variable: which is accessible in the fn1() function only
    localV = 20

    print("Access to the global scope:", myGlobal)
    print("Access to the local scope:", localV)

    # enclosed variable
    enclosedV = 30

    def fn2():
        # another enclosed variable
        enclosedV2 = 40

        print("Access to the enclosed scope:", enclosedV)

        def fn3():
            print("Access to the second enclosed scope in fn3():", enclosedV2)

        fn3()

    fn2()


fn1()
# print("Access to the local scope:", localV) // this will return an error because you can't use the scope outside of the function that it was declared.

print("\n USING SCOPES TO CALCULATE PERIMETER & AREA OF RECTANGLE")

# global variable
codeReports = "Success!!"


def perimeterRectangle(l, b):
    per = 2 * (l + b)
    print(
        "The perimeter of a rectangle of length {0} and breadth {1} = {2}m".format(
            l, b, per
        )
    )

    def areaRectangle():
        # we accessed the enclosed parameters in perimeterRectangle() and used it in our areaRectangle()
        area = l * b
        print(
            "The area of a rectangle of length {0} and breadth {1} = {2}m2".format(
                l, b, area
            )
        )

    areaRectangle()

    # accessing and printing the global variable
    print("Code Reports:", codeReports)


perimeterRectangle(5, 8)
