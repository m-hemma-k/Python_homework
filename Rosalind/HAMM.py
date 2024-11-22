#!/usr/bin/env python3

hamming_distance = 0

s = 'CCGGTTGGTTGCTTCTTATGACCTCTAATCACGCCCCGGGCTCGTAAAATGGGGTAGGAGCAACGGGCTTCGCTTTGGAAAACCGCGACTATAATTAAAGTGCTGCCCAATCCCTGGATTTCAGCCGACAGCACACCGATATTTCTGCCCTCGGCAGGTAAGTTCAGCGGCCTCATTAGCAGGTTGGAGAAAACATCTACCCAGGTGTCGTCACGCTAACGACATCGTCCAACCTAATATCTGCGCGGTTCGCCGAGGTAACATCGTAGCCATCGTAAGGCTCAGTTTGCATTGCCGGTGGATTCCGTGCGACCCAACTCTTAGGTTGCGACTCCCCGTCACTGGTCGCAGGCATCCTAGAACTATATAAGGTCCTCGGGTCAGCGCATACTGCCAACGTTTGCAAACGTTTAGATGCCCGGACAACAGCACCGCGTCACAAATGACCGATTGCTATACTTGACGAGGCAGAATCGTGCACCCAAGGTTTCGGACCAGCCACCAGTTCTTCATTGCATAAGGCTGCGCTAGCACCCTAGGACTGGACTTCTTACTCTGGTTCAAAAGGTATGTTGGGGTCTTGCACATCTGTCGTGGATAATTCTAACTGCCTTGTACGCTTCCAAGACGGACGCCGACACGCGTATGTTCCGGCGTGTGGCTCAAATGTTTGGACTCTGAGCTCAAAGCTACGGACACTGGGATTCACGGCAATTTGTCCTCCTGGCATGTAAAAAGTCGGGCAGATGCGGCCAGCTGATGGCGAAATACTTGAACTTATAGCCCCTTCGCAACTTATATCCGCTCCGCTAATTGAAAATGCGGCGACAGGGCGTGCCAAACGATTAATGATAGCTATGAGACATGTGCACGGTAACTGAGACCTTGAAAAACACACCAGACTAGAAATCTAGCCTCTACTCGCGCCGGTCCTCACGTTTAAGGCAGTGAATTCAACATGGTAGGTAACCCTTGAGATAC'
t = 'TCAGCAGAGTCCGGCTCCAGTTGGTGAAACATTATTCCAATTCCTGTCATTGTGCAGGAGCCGAGAACCTCTCTTCGTCCCCCCGCGACGCTGTTTAGTTTGCTACTCAAGTACTTGATTAGGTGGACCTCCAAGCGGTTCTTTCCTGCCTCGAGGCGTTACATTTGCTGATGAAAGAGGAGGTTGAATTCGGTGTCGACCATGGTGTCGAAACCGCACCTCCAAAGTCTATCCTGGTATCTCTGCGGTTCCTGGGGTTTGAAGCCCTTAATTCGTGATCGTCATGATGGAGTGTTACCACATTCGCTGTGACCGAGTCCTCCGATTGTCAGCCCGTGTCATCGGCGCCAGCCATTTTAAAGTAAGATATGGCAATCGGAAAATCGCATACTCCTACCGTTTGTAAGGGGTCAGTTAACTCACACACGCCATCTGATCAATCATAATTTTTTGTTATGTTGGTCGATCAAGTGTCGTTCTCCGAATGGCCCTACGCTCCCCCGATTTCTACCCAACTTTCAACATCGCATCCACACTACAAAAGGACAAAATCCTACGGATCAAGCATTACGTTGGTGTACAAGAAATGTACAATGAGATATTATCACTGCCTGGTCTGCTTTGGAACCGCGCCGCCAGTGTATACCGGACGACCCTGGGACTAAATCGTATAGAGTCTTAGACGAAGGCTACCATATTTGTTAAGCGCTTCGAAAAGCCCCCGCTGAATTTACCTCTTTCCCCACATTTCGCCGGCTGATGATGAGCTACCAGATCGTATGACGAATTGGCGCCCTATAACCACAGCCCTACTGGCTGATGAGGCATGAATCTTCCCGGGCTTATGTATTTTGACTAACAGCCCGCAGTAAGGAAGGGGATCCCTAGAAGGACACACCATTCGGTTGGTGTAGCACCTTTTCGCGCCGGCACCCAAGATCACGGAAGGTAGTTTTAAGTTGTCAGCAACTCCCGGGATAT'

for i in range(len(s)):
    if s[i] != t[i]:
        hamming_distance += 1

print(hamming_distance)