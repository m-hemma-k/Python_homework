#!/usr/bin/env python3

# Note: This script requires Python 3.12.7

# Define the file path to the input file
filepath = "./rosalind_data/rosalind_ini5.txt"
# Open the file in read mode and assign it to 'infile'
with open(filepath, 'r') as infile:
    lines = infile.readlines()
    # Iterate over each line in the 'lines' list
    for line in lines:
    # Strip whitespace from the beginning and end of each line
        (line.strip())

# Iterate over every second line in the 'lines' list, starting from the second line (index 1)
for l in lines[1::2]:
    # Print each of these lines after stripping whitespace from the beginning and end
    print(l.strip())