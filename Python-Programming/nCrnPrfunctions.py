# A function to calculate combination and permutations
# Combination = nCr


# A function to calculate factorial
def factorial(num):
    fact = 1
    if num < 1:
        return
    for n in range(1, num + 1):
        fact *= n
    return fact


# A function to calculate Combination (nCr - n choose r)
def combination(n, r):
    comb = factorial(n) / (factorial(r) * factorial(n - r))
    print("The nCr with n = {0} and r= {1} = {2}".format(n, r, comb))


combination(5, 2)
combination(17, 6)


print("\n")


# A function to calculate Permutation (nPr)
def permutation(n, r):
    perm = factorial(n) / factorial(n - r)
    print("The nPr with n = {0} and r= {1} = {2}".format(n, r, perm))


permutation(5, 2)
permutation(17, 6)
