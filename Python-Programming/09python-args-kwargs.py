# with args, you can pass any amount of non-keywords variables

# without args


def sum(a, b):
    return a + b


print(sum(10, 20))
# print(sum(10,20,30)) #this will return a type error because the sum() can only take two arguments

# with args, we can take as many arguments
seeds = [1, 2, 3, 34, 4, 5, 6]


def sum1(*args):
    sum = 0
    for x in args:
        sum += x
    print("sum =", sum)


sum1(10, 15, 11, 33, 44, 5, 3)
sum1(*seeds)


# with kwargs, you can pass any amount of keyword arguments (kw-args)
def sum2(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    print("Sum =", sum)


sum2(orange=20.5, mango=45.7, apple=67.3)
