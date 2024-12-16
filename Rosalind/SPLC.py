#!/usr/bin/env python3

# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

# Given: 
# A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. 
# All strings are given in FASTA format.

# Return: A protein string resulting from transcribing and translating the exons of s. 
# (Note: Only one solution will exist for the dataset provided.)

CODONS = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            if line.startswith('>'):
                continue
            else:
                stripped.append(line.strip())
    return stripped

def find_introns(stripped):
    result = ''

    s = stripped[0]
    introns = []

    for i in range(1, len(stripped)):
        introns.append(stripped[i])

    for i in introns:
        s = s.replace(i, '')

    for i in range(0, len(s), 3):
        codon = s[i:i+3]

        protein = None
        if CODONS.get(codon):
            protein = CODONS[codon]
    
        if protein == 'Stop':
            break

        if protein:
            result += protein

    return result

def main():
    # filepath = './rosalind_data/test_SPLC.txt' # testdata
    filepath = './rosalind_data/rosalind_splc.txt'
    data = read_input(filepath)

    protein = find_introns(data)
    print(protein)

if __name__ == '__main__':
    main()