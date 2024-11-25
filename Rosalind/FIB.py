#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

def rabbit_pairs(n, k):
    # Initialize the first two months
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    # Initialize the first two months
    F1 = 1 # the first generation
    F2 = 1 # the first generation matures which gets offspring in the next generation
    
    # Calculate the number of rabbit pairs for each month
    for i in range(3, n + 1):
        Fn = F1 + k * F2 # all rabits + new born rabits which can only be born by F2 generation
        F2 = F1 # F1 matures to F2 and F2 gets offspring the next time
        F1 = Fn # all rabbits are now F1
    return Fn # if n generations are done it will return all the rabbits

# Sample Dataset
n = 31
k = 5

# Calculate the total number of rabbit pairs after n months
result = rabbit_pairs(n, k)
print(result)