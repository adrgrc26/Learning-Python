#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

rc_dna = ''

for i in range(len(dna) -1, -1, -1):
	nt = dna[i]
	if   nt == 'A' : rc_dna += 'T'
	elif nt == 'T' : rc_dna += 'A'
	elif nt == 'C' : rc_dna += 'G'
	elif nt == 'G' : rc_dna += 'C'
	else		   : rc_dna += 'N'

print (rc_dna)



"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
