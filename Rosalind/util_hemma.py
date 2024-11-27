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

def read_fasta(fasta):
    sequences = {}
    current_id = ""
    for line in fasta:
        if line.startswith(">"):
            current_id = line[1:].strip()
            sequences[current_id] = ""
        else:
            sequences[current_id] += line.strip()
    return sequences

def read_oneseq_fasta(fasta_path):
    seq = ""
    with open(fasta_path, 'r') as fasta:
        for line in fasta:
            if line.startswith(">"):
                pass  # Überspringt die Header-Zeilen
            else:
                seq += line.strip()
    return seq