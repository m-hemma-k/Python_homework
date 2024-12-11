#!/usr/bin/env python3

# Given: A DNA string of length at most 1 kbp in FASTA format.

# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        fasta = ''
        for line in lines:
            if line.startswith('>'):
                continue
            else:
                fasta += line.strip()
    return fasta

def rev_comp(fasta):
    comp = ''
    for n in fasta:
        if n == 'A':
            comp += 'T'
        elif n == 'T':
            comp += 'A'
        elif n == 'C':
            comp += 'G'
        elif n == 'G':
            comp += 'C'
        else:
            return None
    return comp[::-1]

def find_restriction(fasta):
    l = len(fasta)
    positions = []
    for i in range(l):
        for j in range(4, 13):
            if i + j <= l:
                dna = fasta[i:i+j]
                if len(dna) >= 4 and dna == rev_comp(dna):
                    positions.append((i + 1, j))
    return positions

def main():
    filepath = './rosalind_data/rosalind_revp.txt'
    data = read_input(filepath)
    positions = find_restriction(data)
    for pos in positions:
        print(f"{pos[0]} {pos[1]}")

if __name__ == '__main__':
    main()