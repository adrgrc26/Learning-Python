#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

GC_PERCENT = 0

for i in range (len(dna)):
	if dna[i] == 'C' or dna[i] == 'G':
		GC_PERCENT+=1
print('%.2f' % (GC_PERCENT/ len(dna)))
print('{:.2f}'.format(GC_PERCENT/len(dna)))
print(f'{GC_PERCENT/len(dna):.2f}')
		


"""
python3 gc.py
0.42
0.42
0.42
"""
