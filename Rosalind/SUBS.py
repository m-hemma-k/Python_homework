#!/usr/bin/env python

# Finding a Motif in DNA:
# Given two strings s = s1 s2 ... sn and t = t1 t2 ... tm where m ≤ n, t is a
# substring of s if t is contained as a contiguous collection of symbols in s.
# 
# The position of a symbol in a sequence is the total number of symbols found to
# its left, including itself (e.g., the positions of all occurrences of U in
# AUGCUUCAGAAAGGUCUUACG are 2, 5, 6, 15, 17, and 18). The symbol at position i
# of s is denoted by s[i]. For that matter, a substring of s can be represented
# as s[j:k], where j and k represent the starting and ending positions of the
# substring in s.
# 
# The location of a substring is its beginning position; note that t will have
# multiple locations in s if it occurs more than once as a substring of s (see
# the Sample sections below).
# 
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