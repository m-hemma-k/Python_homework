# !/usr/bin/env python3

# Red-Nosed Reports
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

# read input
# is it fluctuating
# is it ascending
# is it descending

# read out the input file
# it will result in a lists within a list which are numbers as strings
def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

# convert the numbers from strings to integers
def parse_data(stripped_list):
    data = []
    for line in stripped_list:
        line_data = []
        for x in line.split():
            line_data.append(int(x))
        data.append(line_data)
    return data

# check if the numbers in one list are ascending and return true if so
def ascending(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

# check if the numbers in one list are descending and return true if so
def descending(l):
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            return False
    return True

# combine ascending and descending
def monotonic(l):
    return ascending(l) or descending(l)

# check if the numbers are within the tolerance
def within_tolerance(l):
    for i in range(len(l)-1):
        diff = abs(l[i] - l[i+1])
        if not (diff > 0 and diff < 4):
            return False
    return True

# main function
def main():
    raw = read_input('./data/day2_test.txt')
    data = parse_data(raw)
    # data = [[int(x) for x in line.split()] for line in raw]

    safe_reports = 0
    for report in data:
        if monotonic(report) and within_tolerance(report):
            safe_reports += 1
    print(safe_reports)

if __name__ == '__main__':
    main()