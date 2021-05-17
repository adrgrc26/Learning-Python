#!/usr/bin/env python3

import argparse
import mcb185
import random

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?


##Are ORFs genes? 
# People often use length threshold. 
# At what threshold oes it pick up? 
#What's likely and unlikely to happen? 
# LEt's get an idea of what random background happens. 
#generate random sequence
#little bit of a mixture between birthday problem and modern .
# it's a histogram. 
# here are the reads piling up in different places. '

# setup
parser = argparse.ArgumentParser(description='explore open reading frame length.')
# required arguments
parser.add_argument('--size', required=False, type=int, default=4500000,
	metavar='<int>', help='genome size [%(default)i]')
parser.add_argument('--orfmin', required=False, type=int, default=100,
	metavar='<int>', help='minimum open reading frame length [%(default)i]')
parser.add_argument('--gc', required=False , type=float, default =0.5,
	metavar='<float>', help='gc fraction [%(default).3f]')

#switches
parser.add_argument('--info', action='store_true',
	help='provide additional info')
parser.add_argument('--seed', action='store_true',
	help='fix random seed')
# optional arguments with default parameters


# finalization
arg = parser.parse_args()

#get same random numbers every time you run the program
if arg.seed: random.seed(1)

if arg.info: print(arg.size, arg.orfmin, arg.gc)
#print(arg.size, arg.orfmin, arg.gc)
# testing

seq = mcb185.randseq(arg.size, arg.gc)
#print(seq)


#look for ATG
lengths = []
for i in range(len(seq) -2):
	start = None
	stop = None
	if seq[i: i +3] == 'ATG': 
		start = i
		for j in range(i, len(seq) -2, 3):
			codon = seq[j: j +3]
			if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
				stop = j
				break
	if stop != None: lengths.append((stop - start)/3)
count = 0
for n in lengths:
	if n> arg.orfmin:
		count += 1
print(count)


lengths = [int(a) for a in lengths] #; all values are floating point. make integers



##histogram

for x in range(len(lengths)):
	dup = 0
	for y in range(len(lengths)):
		if lengths[x] == lengths[y]:
			dup += 1
		else: 
			y += 1
	print(lengths[x], dup)
print(lengths)

###Worked on with Victoria Rees


