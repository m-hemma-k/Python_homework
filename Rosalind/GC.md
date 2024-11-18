# **Homework by Hemma Kargl**
### Course: **2024W 300160-1 Practical introduction to programming for biologists**
#### Section: Rosalind GC section
#### Date: 18.11.2024

## **PROBLEM:**
#### The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
#### For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
#### DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. 
#### In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; 
#### the first line to begin with '>' indicates the label of the next string.

#### In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

## **Given:**
#### At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

## **Return:** 
#### The ID of the string having the highest GC-content, followed by the GC-content of that string. 
#### Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
```
Rosalind_0808
60.919540
```

## *TACKLE THE PROBLEM:*

### 1. Think of the problem in a smaller way:
#####    Use a simple, short sequence and calculate the GC content from it and make a function.
#####    --> We can use the GC calculator function later on.
#####    - Count the occurrences if 'G' and 'C'.
#####    - Calculate the total number of GC pairs.
#####    - Calculate the length of the sequence.
#####    - Calculate the percentage.
```
def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100
```

### 2. Making a function for the highest GC content.
#####   - Iniate the variables with none and 0.
#####   - Loop over sequences to find the sequence with the highest GC percentage.
```
def find_highest_gc_content(gc_contents):
    highest_gc_sequence = None
    highest_gc_percentage = 0
    for name, gc_percentage in gc_contents.items():
        if gc_percentage > highest_gc_percentage:
            highest_gc_percentage = gc_percentage
            highest_gc_sequence = name
    return highest_gc_sequence, highest_gc_percentage
```

### 3. Look up in the internet how to read out fasta file formats.
```
def read_sequences(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            sequences[record.id] = str(record.seq)
    return sequences
```

### 4. Put all the functions together and print out the result.
```
def main(file_path):
    sequences = read_sequences(file_path)

    gc_contents = {}
    for name, seq in sequences.items():
        gc_contents[name] = calculate_gc_content(seq)
    highest_gc_sequence, highest_gc_percentage = find_highest_gc_content(gc_contents)
    print(highest_gc_sequence)
    print("{:.6f}".format(highest_gc_percentage))

file_path = "./rosalind_data/rosalind_GC.txt"
main(file_path)
```