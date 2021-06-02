import argparse
import mcb185
import statistics

parser = argparse.ArgumentParser(description='stats about sequence')
# required arguments
parser.add_argument('--file', required=True, type=str, #--r1 = string
	metavar='<str>', help='required fasta file')
arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file) :
	#print(name, len(seq))
	length.append(len(seq))

length.sort()
#print(length)

#Min
print('min is',min(length))

#max
print('max is',max(length))

#sum
#sum = 0
#for value in length: 
#	sum += value

print('sum is', sum(length))

#mean
print('mean is', statistics.mean(length))

print('median is', statistics.median(length))

#n50 not available!


print('n50 is', mcb185.n50(length))
#print(length)
#n50 - sum values, once it is greater than 1/2 the total, that is the n50


