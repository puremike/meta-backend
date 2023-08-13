num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

# print each value in the num_list in sequential order
for m in num_list:
    print(m, end=" ")

print("\n")

for n in num_list:
    # print values that are greater than 45 only
    if n > 45:
        print(n, end=" ")

    # print values that are less than 45 only
    elif n < 45:
        print(n, end=" ")

    # if n>= 45:
    #     print(n)
print("\n")
# print the index of each values
for ind in enumerate(num_list):
    print(ind)
