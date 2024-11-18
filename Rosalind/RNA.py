#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

# PROBLEM: An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

"""
# Given: A DNA string t having length at most 1000 nt.
filepath = "./rosalind_data/rosalind_RNA.txt"

# Open the file in read mode and assign it to 'infile'
with open(filepath, 'r') as infile:
    # Read line from the file
    sequence = infile.readline().strip()


# Return: The transcribed RNA string of t.
RNA = sequence.replace("T", "U")
print(RNA)
"""

sequence = 'GATGGAACTTGACTACGTAAATT'
RNA = ''

for nt in sequence:
    if nt == 'T':
        RNA += 'U'
    else:
        RNA += nt

print(RNA)
    