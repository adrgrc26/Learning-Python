#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

"""
#create list of bps with random length, then just plug everything into eqn. for coverage?
# is your for loop necesary? 
# # is COVERAGE just
#  (Read lengths *Read number)    /genome size  ? What am I doing for read?
# You need to build random read coverage first
"""


import sys
import random

genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_length = int(sys.argv[3])

#clean slate; make empty genome
#make reads; generate random reads
#get length--add genome counts over the length of however big the read is
#count up areas of minimum,maxima of avg cover
cov = [] #make empty genome (30-32)
for i in range(genome_size):
	cov.append(0)

#make random reads(x= read_num)
for i in range (read_num):
	start = random.randint(0, genome_size - read_length )
	#print(start)
	end = start + read_length
	for coor in range (start,end):
		cov[coor] += 1 # the coverage at coordinate is increasing by 1
		
minimum = cov[read_length]
maximum = cov[read_length]
total = 0
#for j in range (read_length, genome_size - read_length)
for count in cov[read_length:-read_length]:
	if count < minimum : minimum = count
	if count > maximum : maximum = count
	total += count

print (minimum, maximum, total/(genome_size - 2*read_length))
	#for j in range (read_length, ):
		
#
# where it starts and it has a length (every read needs a random starting point))







"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
