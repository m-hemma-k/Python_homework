#!/usr/bin/env python3

# a library of utility functions for Rosalind exercises

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

def read_sequence(filepath):
    with open(filepath, 'r') as infile:
        sequence = infile.readline().strip()
    return sequence

def complement (sequence):
    for nt in sequence:
        if nt == 'A':
            return'T'
        elif nt == 'T':
            return'A'
        elif nt == 'C':
            return'G'
        else:
            return'C'