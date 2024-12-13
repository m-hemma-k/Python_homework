#!/usr/bin/env python3

# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

# Given: 
# A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. 
# All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. 
# (Note: Only one solution will exist for the dataset provided.)

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            if line.startswith('>'):
                continue
            else:
                stripped.append(line.strip())
        s = stripped[0]
        a = stripped[1]
        b = stripped[2]
    return s, a, b

def find_introns(string, introns):
    
    return exon

def main():
    filepath = './rosalind_data/test_SPLC.txt'
    s, a, b = read_input(filepath)


    # test:
    print(s, a, b)

if __name__ == '__main__':
    main()