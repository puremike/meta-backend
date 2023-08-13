a = "Mike"
print(len(a))

# concatenation of string
c = "Hello"
d = "Michael"
print(c + " " + d + "!")

# indexing a string
print(a[1 - 3])
print(a[:4])
print(d[4])

# convert a number to a string
e = 55
f = str(e)  # type casting
print(
    type(f) == str
)  # checking if the condition is true or false (string or no-string)

# reverse a string
nString = "enola"
print("reversed string:", nString[::-1])
print("reversed string:", "".join(reversed(nString)))

# convert a string to upper and lowercase
print("lower:", nString.lower())
print("upper:", nString.upper())

# capitalize a string
print("capitalize string:", nString.capitalize())

# split a string and return a list of it
mString = "Welcome to lagos, Nigeria"
print(mString.split())

# isLower(), isUpper(), isCapitalize(), is..........

# find() -Searches the string for a specified value and returns the position of where it was found
print("find:", mString.find("Nigeria"))

# strip() - trim a string
sString = "    Welcome boys!   "
print("trimmed string:", sString.strip())

# join() to join an iterable to a string
pString = ["michael12", "gmail.com"]
print("@".join(pString))
