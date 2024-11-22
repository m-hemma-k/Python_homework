#!/usr/bin/env python

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# 
# Return: All locations of t as a substring of s.
# 
# Sample Dataset:
# GATATATGCATATACTT
# ATAT
# 
# Sample Output:
# 2 4 10


def motif_count(sequence_and_motif):
    results = []

    sequence, motif = sequence_and_motif.split()
    motif_length = len(motif)

    for i in range(len(sequence) - motif_length):
        if sequence[i:i+motif_length] == motif:
            results.append(i + 1)

    return results

# sequence_and_motif = "GATATATGCATATACTT\nATAT"
'''
This was the testing sequence, please ignore.
'''
sequence_and_motif = open('./rosalind_data/rosalind_subs.txt').read()

results = motif_count(sequence_and_motif)
print(' '.join(map(str, results)))
print(len(results)) # also wanted to print how many times the motif was inside the string (just for fun - please ignore)
