#!/usr/bin/env python
# 02_rna_replace.py

# Open input file of dna
with open('data/rosalind_rna.txt', 'r') as input:
	# Whitespace located at the end of the dna seq
	dna = input.read().strip()

# Write output file with transcribed rna
with open('output/q2_rna.txt', 'w') as output:
	output.write(dna.replace('T', 'U'))