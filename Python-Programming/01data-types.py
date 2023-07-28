# In python we have 5 data types, namely:
#     Numeric:
#         Integer
#         Float
#         Complex Number

#     Sequence:
#         String
#         List
#         Tuples

#     Dictionary

#     Boolean

#     Set

a = 10.5
print(type(a))  # float

b = 10
print(type(b))  # integer

c = True
print(type(c))  # boolean


fullName = "Michael Egbinola"
print(type(fullName))  # String

personalDetails = ["Michael", "Egbinola", 24, "Student"]
print(type(personalDetails))  # List == Array

unionSet = {1, 2, 3, 4, 4, 2, 5, 5, 6}
print(unionSet)
print(type(unionSet))  # set


myTuple = (
    "Orange",
    "Mango",
    "Apple",
)  # tuples are immutable after they've been created. It also allows for duplicate values
print(myTuple)
print(type(myTuple))  # tuple

# dictionaries in Python are like objects in JavaScript
data = {
    "firstName": "Michael",
    "lastName": "Egbinola",
    "Occupation": "Backend and Cloud Engineer",
    "Location": "Nigeria",
}
# print(data.keys())
# print(data.values())
for key in data:
    print(key)
for value in data.values():
    print(value)
print(data["Occupation"])
print(type(data))
