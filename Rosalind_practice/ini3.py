#!/usr/bin/env python3

# Given: A string s of length at most 200 letters and four integers a, b, c and d.

# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
# In other words, we should include elements s[b] and s[d] in our slice.

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
        string = stripped[0]
        numbers = stripped[1]
        a, b, c, d = map(int, numbers.split())
    return string, a, b, c, d

def slice_string(string, a, b, c, d):
    slice_1 = string[a:b+1]
    slice_2 = string[c:d+1]
    print(slice_1,slice_2)

def main():
    filepath = './data/rosalind_ini3.txt'
    string, a, b, c, d = read_input(filepath)
    slice_string(string, a, b, c, d)

if __name__ == '__main__':
    main()