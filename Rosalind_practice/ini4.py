#!/usr/bin/env python3

# Given: Two positive integers a and b (a<b<10000).

# Return: The sum of all odd integers from a through b, inclusively.

# You can use a % 2 == 1 to test if a is odd.

# Sample Dataset: 100 200
# Sample Output: 7500

def read_input(filepath):
    with open(filepath, 'r') as infile:
        line = infile.readline()
        a, b = map(int, line.split())
    return a, b

def odd_integer(a, b):
    sum = 0
    for odd in range(a, b):
        if odd % 2 == 1:
            sum += odd
        else:
            continue
    return sum

def main():
    # filepath = './data/test_ini4.py' # testinput
    filepath = './data/rosalind_ini4.txt'

    a, b = read_input(filepath)
    print(a, b)

    sum = odd_integer(a, b)
    print(sum)

if __name__ == '__main__':
    main()