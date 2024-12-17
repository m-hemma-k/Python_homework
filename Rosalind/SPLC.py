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

def read_fasta(path):
    sequences = []
    current_sequence = ""

    with open(path, 'r') as fasta:
        for line in fasta:
            line = line.strip()
            
            if line.startswith(">"):
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
            else:
                current_sequence += line

        if current_sequence:
            sequences.append(current_sequence)

    return sequences

def find_introns(stripped):
    s = stripped[0]
    introns = stripped[1:]

    for i in range(1, len(stripped)):
        introns.append(stripped[i])

    for i in introns:
        s = s.replace(i, '')

    return s

def translate(cds):
    protein = ''
    for i in range(0, len(cds), 3):
        codon = cds[i:i+3]

        aa = None
        if CODONS.get(codon):
            aa = CODONS[codon]
    
        if aa == 'Stop':
            break

        if aa:
            protein += aa

    return protein

def main():
    # filepath = './rosalind_data/test_SPLC.txt' # testdata
    filepath = './rosalind_data/rosalind_splc.txt'
    data = read_fasta(filepath)

    cds = find_introns(data)
    protein = translate(cds)
    print(protein)

if __name__ == '__main__':
    main()