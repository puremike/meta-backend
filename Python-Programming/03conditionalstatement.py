import math
#if, elif, else statement
a = 2
b = 3
c = 5
if(b > a and c >= b):
    print(True)
else: 
    print(False)
print(a > c)

#another if else statement
#Light is currently off
current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')



#Switch Statement
anyNumber = int(input("Enter a positive number to check even or odd: "))
match (anyNumber % 2):
    case 0:
        print(anyNumber, "is an EVEN number!!")
    case 1: 
        print(anyNumber, "is an ODD number!!")
    case default: 
        print("Enter a valid positive number:::::")
    
    


    

