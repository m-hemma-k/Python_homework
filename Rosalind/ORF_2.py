#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

CODON_DICT = {
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

from util_hemma import complement
from util_hemma import read_oneseq_fasta

def rev_complement (sequence):
    dna_rev_comp =''
    for nt in sequence:
        dna_rev_comp += complement(nt)
    return(dna_rev_comp[::-1])

def orf_find(dna_sequence):
    orfs = []
    motif_length = len('ATG')

    for i in range(len(dna_sequence) - motif_length):
        if dna_sequence[i:i+motif_length] == 'ATG':
            orfs.append(i)
    return orfs

def translate(index, sequence):
    protein_sequences = []
    for i in index:
        found_stop = False
        protein_seq = ''
        l = len(sequence)
        for j in range(i, l, 3):
            codon = sequence[j:j+3]
            if len(codon) < 3:
                break
            protein = CODON_DICT.get(codon)
            if not protein:
                break
            if protein == 'Stop':
                found_stop = True
                break
            protein_seq += protein
        if found_stop:
            protein_sequences.append(protein_seq)
    return protein_sequences

dna_sequence = read_oneseq_fasta("./rosalind_data/rosalind_orf.txt")
reverse_dna = (rev_complement(dna_sequence))

orf_index = orf_find(dna_sequence)
orf_index_rev = orf_find(reverse_dna)

proteins_fw = translate(orf_index, dna_sequence)
proteins_rv = translate(orf_index_rev, reverse_dna)

print("\n".join(set(proteins_fw + proteins_rv)))