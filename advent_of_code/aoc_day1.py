#!/usr/bin/env python3

# make test input before that
# two list of numbers
# read the lists --> read input gives us list of lines --> than for line in <extract> --> split function, then we convert the strings to numbers
# sort the lists
# absolute difference abs()
# sum the differences sum(list) or res += diff

file = './data/aoc_day1.txt'

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

raw = read_input(file)

list_a = []
list_b = []
for line in raw:
    rawinput = line.split(' ')
    a = int(rawinput[0])
    b = int(rawinput[-1])
    list_a.append(a)
    list_b.append(b)

list_a.sort()
list_b.sort()

sum_of_differences = 0
for a, b in zip(list_a, list_b):
    diff = abs(a - b)
    sum_of_differences += diff
print(sum_of_differences)



