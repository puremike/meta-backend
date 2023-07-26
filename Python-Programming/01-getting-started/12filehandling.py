#There are two file handling functions in python, namely open and close. The open function is used for reading, writing and creating files.


# ***OPEN FUNCTION***

#open(<FILE_NAME> or <FILE_LOCATION>, <MODE>) --- accepts 2 arguments

#The <MODE> indicates what action is required such as reading, writing or creating. It's also specifies if you want the file output in text or binary format

#<MODE> options:
#mode = 'r' - reading only
# mode = 'r+' - reading and writing
# mode = 'w' - writing only
# mode = 'a' - editing and appending files

# ***CLOSE FUNCTION***
#the close function doesn't take any argument.
#You can also use the close function using the 
# "with open("testing.txt", r) as file" - close the file automatically

#FILE OPENING

file = open("./Python-Programming/01-getting-started/text.txt", "r")
data = file.readline() #reads only 1 line
print(data)
file.close()

print("\n")
#using the - with open() which closes the file automatically. Also works better with exceptional handling
try:
    with open("./Python-Programming/01-getting-started/11exceptionalhandling.py", "r") as f:
        print(f.read()) #reads the entire file
except Exception as e:
    print("Invalid directory or file;", e)

#CREATING FILES

print("\n")
with open("./Python-Programming/01-getting-started/file.txt", "w") as f:
    f.write("Learning file handling - creating a single-line file")

#write multiline with the writelines()
with open("./Python-Programming/01-getting-started/hello.py", "w") as file:
    file.writelines(["x = 'michael'", "\nprint(x)", "\ny = 198", "\nprint(y ** 2)"])

