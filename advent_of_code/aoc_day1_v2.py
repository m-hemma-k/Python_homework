#!/usr/bin/env python3

# The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
# The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
# The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
# The fourth number, 1, also does not appear in the right list.
# The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
# The last number, 3, appears in the right list three times; the similarity score again increases by 9.

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

sum_of_occurrences = 0
for number in list_a:
    count = list_b.count(number)
    sum_of_occurrences += (count * number)
print(sum_of_occurrences)