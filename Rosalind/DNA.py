#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

# PROBLEM: A string is simply an ordered collection of symbols selected from some alphabet and formed into a nt; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.
filepath = "./rosalind_data/rosalind_DNA.txt"

# Open the file in read mode and assign it to 'infile'
with open(filepath, 'r') as infile:
    # Read line from the file
    sequence = infile.readline().strip()

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
nt_count = {}

for nt in sequence:
    if nt in nt_count:
        nt_count[nt] += 1
    else:
        nt_count[nt] = 1

print(nt_count["A"],nt_count["C"],nt_count["G"],nt_count["T"])