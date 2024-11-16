#!/usr/bin/env python3

# Note: This script requires Python 3.12.7

# first, read the file!
filepath = "../rosalind_data/ini5.txt"
with open(filepath, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        print(line.strip())

for l in lines[1::2]:
    print(l.strip())