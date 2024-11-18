#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

from Bio import SeqIO

def read_sequences(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            sequences[record.id] = str(record.seq)
    return sequences

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def find_highest_gc_content(gc_contents):
    highest_gc_sequence = None
    highest_gc_percentage = 0
    for name, gc_percentage in gc_contents.items():
        if gc_percentage > highest_gc_percentage:
            highest_gc_percentage = gc_percentage
            highest_gc_sequence = name
    return highest_gc_sequence, highest_gc_percentage

def main(file_path):
    sequences = read_sequences(file_path)
    gc_contents = {}
    for name, seq in sequences.items():
        gc_contents[name] = calculate_gc_content(seq)
    highest_gc_sequence, highest_gc_percentage = find_highest_gc_content(gc_contents)
    print(highest_gc_sequence)
    print("{:.6f}".format(highest_gc_percentage))

file_path = "./rosalind_data/rosalind_GC.txt"
main(file_path)