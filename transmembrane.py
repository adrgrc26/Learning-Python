#!/usr/bin/env python3


import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa


#Read Fasta files

name = []
proteins = []

with open(sys.argv[1]) as fp:
	seq = []
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			words = line.split()
			name.append(words[0][1:])
			if len(seq) > 0: proteins.append(''.join(seq))
			seq = []
		else:
			seq.append(line)
	proteins.append(''.join(seq))

#fxn to calculate hydrophobicity score of protein seqs
def kd(seq):
	kd = 0 
	for aa in seq:
		if	aa == 'A': kd += 1.8
		elif aa == 'C': kd += 2.5
		elif aa == 'D': kd += -3.5
		elif aa == 'E': kd += -3.5
		elif aa == 'F': kd += 2.8
		elif aa == 'G': kd += -0.4
		elif aa == 'H': kd += -3.2
		elif aa == 'I': kd += 4.5
		elif aa == 'K': kd += -3.9
		elif aa == 'L': kd += 3.8
		elif aa == 'M': kd += 1.9
		elif aa == 'N': kd += -3.5
		elif aa == 'P': kd += -1.6
		elif aa == 'Q': kd += -3.5
		elif aa == 'R': kd += -4.5
		elif aa == 'S': kd += -.8
		elif aa == 'T': kd += -0.7
		elif aa == 'V': kd += 4.2
		elif aa == 'W': kd += -0.9
		elif aa == 'Y': kd += -1.3
	return kd/len(seq)

#Fxn identihying hphbc helices(hel); window length; and hydrophobicity score ; Start building in 67

#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

def hel(seq, w, t):
	for i in range(len(seq)-w+1):
		pep = seq[i:i+w]
		if kd(pep) > t and 'P' not in pep:
			return True
	return False


for name, seq in zip(name, proteins):
	nterm = seq[:30]
	cterm = seq[30:] #(aa range)
	if hel(nterm, 8,2.5) and hel(cterm,11,2): #(end, signal peptide, kd cap)
		print(name)





"""
	
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
