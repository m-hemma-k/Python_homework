#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

# PROBLEM: In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

"""
# Given: A DNA string s of length at most 1000 bp.
filepath = "./rosalind_data/rosalind_REVC.txt"

# Open the file in read mode and assign it to 'infile'
with open(filepath, 'r') as infile:
    # Read line from the file
    sequence = infile.readline().strip()

sequence = 'AAAACCCGGT'

# Return: The reverse complement sc of s.
complement = ''
for nt in sequence:
    if nt == 'A':
        complement += 'T'
    elif nt == 'T':
        complement += 'A'
    elif nt == 'C':
        complement += 'G'
    else:
        complement += 'C'

print(complement[::-1])
"""

from util import complement

sequence = 'AAAACCCGGT'
sequence_comp =''

for nt in sequence:
    sequence_comp += complement(nt)

print(sequence_comp[::-1])