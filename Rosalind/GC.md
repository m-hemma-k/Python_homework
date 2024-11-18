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
#####    - Define one short DNA sequence as a string.
#####    - Count the occurrences if 'G' and 'C'.
#####    - Calculate the total number of GC pairs.
#####    - Calculate the length of the sequence.
#####    - Calculate the percentage.
#####    - The output in Rosalind is 6 decimal places.
```
def calculate_gc_content(dna_string):
    g_count = dna_string.count('G')
    c_count = dna_string.count('C')
    gc_pairs = g_count + c_count
    nt_counts = len(dna_string)
    gc_percentage = (gc_pairs / nt_counts) * 100
    return gc_percentage

sequence = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

gc_content = calculate_gc_content(sequence)
print("{:.6f}".format(gc_content))
```

### 2. We can now make the problem bigger by using more than one sequence and identifying the DNA string with the highest GC content.
#####    --> Output: The DNA sequence name with the highest GC content and the percentage.
#####    - The sequences are put in a dictionary.
#####    - Before we put anything in a function, we have to take a closer look at the FASTA format file input and potentially modify.
```
sequences = {
    "Sequence 1": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT",
    "Sequence 2": "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
    "Sequence 3": "ATGCCAGTAGCTAGCTAGCTGACTGATCGTAGCTAGCTAGCTGACTGATCGTAGCTAGCTAGCTGACTGATCGTAGCTAGC"
}

gc_contents = {}
for name, sequence in sequences.items():
    gc_contents[name] = calculate_gc_content(sequence)

# Initialize variables to keep track of the highest GC content and corresponding sequence name
highest_gc_sequence = None
highest_gc_percentage = 0

# Iterate over the gc_contents dictionary
for name, gc_percentage in gc_contents.items():
    if gc_percentage > highest_gc_percentage:
        highest_gc_percentage = gc_percentage
        highest_gc_sequence = name

# Print the result
print(highest_gc_sequence) 
print("{:.6f}".format(highest_gc_percentage))
```

### 3. Look up in the internet how to read out fast file formats.
#####    -
#####    - 
#####    - 
```
def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        sequence_name = ""
        sequence_data = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_name:
                    sequences[sequence_name] = sequence_data
                sequence_name = line[1:]  # Remove the '>' character
                sequence_data = ""
            else:
                sequence_data += line
        if sequence_name:
            sequences[sequence_name] = sequence_data
    return sequences

# Example usage
file_path = "path_to_your_file.txt"
sequences = read_fasta(file_path)
```