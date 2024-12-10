#!/usr/bin/env python3

# Find XMAS:
# horizontal, 
# vertical, 
# diagonal, 
# written backwards, 
# or even overlapping other words

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

def find_horizontal(word, text):
    occurences = 0
    for line in text:
        occurences += line.count(word)
    return occurences

def find_vertical(word, text):
    columns = [''] * len(text)
    for line in text:
        for i, letter in enumerate(line):
            columns[i] += letter
    occurences = 0
    occurences += find_horizontal(word, columns)
    return occurences

def find_diagonal(word, text):
    n = len(text)
    dr_diagonals = []

    for i in range(n):
        diag = ''
        x, y = i, 0
        while x < n and y < n:
            diag += text[x][y]
            x += 1
            y += 1
        dr_diagonals.append(diag)

    for j in range(1, n):
        diag = ''
        x, y = 0, j
        while x < n and y < n:
            diag += text[x][y]
            x += 1
            y += 1
        dr_diagonals.append(diag)

    occ = find_horizontal(word, dr_diagonals)
    return occ

def find_backwards(word, text):
    backwards = []
    occ = 0
    for lines in text:
        backwards.append(lines[::-1])
    occ = find_horizontal(word, backwards)
    return occ

def main():
    filepath = './data/day4.txt'
    data = read_input(filepath)

    hor_forw = find_horizontal('XMAS', data)
    hor_back = find_horizontal('SAMX', data)

    ver_forw = find_vertical('XMAS', data)
    ver_rev = find_vertical('SAMX', data)

    diag_forw = find_diagonal('XMAS', data)
    diag_rev = find_diagonal('SAMX', data)

    back_forw = find_backwards('XMAS', data)
    back_rev = find_backwards('SAMX', data)

    total = hor_forw + hor_back + ver_forw + ver_rev + diag_forw + diag_rev + back_forw + back_rev
    print(total)


if __name__ == '__main__':
    main()