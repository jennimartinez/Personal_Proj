#!/usr/bin/env python
# 01_count_dna.py

# Open file
with open('data/rosalind_dna.txt', 'r') as input:
	dna = input.read()

# Create empty list
nucleo_count = []

# Append count of each nucleotide into nucleo_count
for nucleotide in ['A', 'C', 'G', 'T']:
	nucleo_count.append(str(dna.count(nucleotide)))

# Check answers
print ' '.join(nucleo_count)

with open('output/q1_dna_count.txt', 'w') as output:
	output.write(' '.join(nucleo_count))
