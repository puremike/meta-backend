#A function to check if a number is a perfect square
import math
def isSquared(n):
    if n<0:
        return
    elif(math.sqrt(n) % 1 == 0):
        print("{0} is a perfect square!!".format(n))
isSquared(4)
    

#to check even or odd number
def checkOddEven(num): 
    if num<1:
        return
    elif (num % 2 == 0):
        print(num, "is an even number!!!")
    elif(num % 2 == 1):
          print("{0} is an odd number!!!".format(num))
checkOddEven(4)
checkOddEven(100)
checkOddEven(35)

# print(type(checkOddEven)) //function

#a function using for loop to calculate the sum of number from 1 to 20
def sumNumbers(num):
    
    sum = 0  
    for i in range(num+1):
        sum += i
    print("The sum of numbers from 1 - 20 = ", sum)

sumNumbers(5)
sumNumbers(500)
sumNumbers(230)
sumNumbers(500)