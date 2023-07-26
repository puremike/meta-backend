import math
try:
    y = 25
    print("y =", y)
    print("x =", x) #return an error because x is not defined
except Exception as e:
    print("x is not defined;", e)
finally:
  print("The 'try except' is finished")

print("\n")
try:
    items = [1,2,3,4,5]
    item = items[6]
    print("item =", item)
except Exception as e:
    print("Index errror;", e)

print("\n")
try:
    def divideNum(a,b):
        return a/b
    print(divideNum(100,10))
    print(divideNum(40, 0)) #it will return a DivisionByZero Error
except Exception as e:
    print("division error;", e)

print("\n")
try:
    #a function to check is a number is a perfect square
    def checkIsSquared(n):
        if n < 0:
            return
        elif (math.sqrt(n) % 1 == 0):
            print(n, "is a perfect square!!")
        else:
            print(n, "is not a perfect square!!!")
    checkIsSquared(4)
    checkIsSquared(5.5)
    checkIsSquared("A") #return an error
except Exception as e:
    print("the argument must be a integer;", e)