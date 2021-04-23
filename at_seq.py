#!/usr/bin/env python3

import random
random.seed(343) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

bp = 30
seq = ''
at = 0.6
at_count = 0 
for i in range(bp):
	r = random.random()
	if r < at:
		at_count += 1
		r = random.random()
		if r < 0.5: seq += 'a'
		else:	    seq += 't'
	else:
		r = random.random()
		if r < 0.5: seq += 'c'
		else: 		seq += 'g'
	
print(bp, at_count/bp, seq)





"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
