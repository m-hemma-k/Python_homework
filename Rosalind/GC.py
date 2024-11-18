#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

def calculate_gc_content(dna_string):
    g_count = dna_string.count('G')
    c_count = dna_string.count('C')
    gc_pairs = g_count + c_count
    nt_counts = len(dna_string)
    gc_percentage = (gc_pairs / nt_counts) * 100
    return gc_percentage

sequences = {
    "Sequence 1": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT",
    "Sequence 2": "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
    "Sequence 3": "ATGCCAGTAGCTAGCTAGCTGACTGATCGTAGCTAGCTAGCTGACTGATCGTAGCTAGCTAGCTGACTGATCGTAGCTAGC"
}

gc_contents = {}
for name, sequence in sequences.items():
    gc_contents[name] = calculate_gc_content(sequence)

# Initialize variables to keep track of the highest GC content and corresponding sequence name
highest_gc_sequence = None
highest_gc_percentage = 0

# Iterate over the gc_contents dictionary
for name, gc_percentage in gc_contents.items():
    if gc_percentage > highest_gc_percentage:
        highest_gc_percentage = gc_percentage
        highest_gc_sequence = name

# Print the result
# Print the result
print(highest_gc_sequence) 
print("{:.6f}".format(highest_gc_percentage))