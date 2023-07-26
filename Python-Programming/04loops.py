import time
#start time
startTime = time.time()

#FOR LOOP

#looping a string
str = "Amt"
for st in str:
    print(st, end=" ") #will loop through and print in one line
    
print("\n")

#looping through numbers
for i in range(1,6):
    print(i)
    
print("\n")

#nested for loop
strN = "Me"
strM = "No"
for n in strN:
    for s in strM:
        print(n,s)

print("\n")

#loop through a list
fruits = ["Mango", "Apple", "Orange", "Watermelon"]

for fr in fruits:
    print("I love", fr)


print("\n")

#for loop to calculate the sum of number from 1 to 20
sum = 0
number = int(input("Enter a valid number to get the sum from 1 to the number: "))
    
for i in range(number+1):
    sum += i
print("The sum of numbers from 1 - 20 = ", sum)
  
print("\n")

#WHILE LOOP
count = 0
while count < len(fruits):
    print("I love", fruits[count])
    count += 1

#looping through numbers using while loop



count2 = 1
sum = 0
while count2 <= 5:
    sum += count2
    count2+=1
print(sum, "\n")

#end time
print(round((time.time() - startTime), 2))
    