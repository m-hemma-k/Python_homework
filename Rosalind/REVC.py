#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

# PROBLEM: In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.
filepath = "./rosalind_data/rosalind_REVC.txt"

# Open the file in read mode and assign it to 'infile'
with open(filepath, 'r') as infile:
    # Read line from the file
    sequence = infile.readline().strip()

# Return: The reverse complement sc of s.
reverse_complement = ''
for nt in sequence:
    if nt == 'A':
        reverse_complement += 'T'
    elif nt == 'T':
        reverse_complement += 'A'
    elif nt == 'C':
        reverse_complement += 'G'
    else:
        reverse_complement += 'C'

print(reverse_complement[::-1])