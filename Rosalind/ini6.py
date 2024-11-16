#!/usr/bin/env python3
# Note: This script requires Python 3.12.7

# Given: A string s of length at most 10000 letters.
# Define the file path to the input file
filepath = "./rosalind_data/rosalind_ini6.txt"

# Open the file in read mode and assign it to 'infile'
with open(filepath, 'r') as infile:
    # Read line from the file
    s = infile.readline().strip()
    # Split the line into words based on spaces
    words = s.split(' ')

# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(key, value)