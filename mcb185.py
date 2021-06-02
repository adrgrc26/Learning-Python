

def read_fasta(filename):
	name = None
	seq = []
	
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			elif line.startswith('>'):
				if len(seq) > 0: # now is the time to return name, seq
					yield name, ''.join(seq)
				words = line.split()
				name = words[0][:]
				seq = []
			else:
				line = line.rstrip()
				seq.append(line)
	yield name, ''.join(seq)

#gc content
def gc(dna): 
	g = dna.count('G')
	c = dna.count('C')
	return (g+c)/len(dna)
#n50
def n50(length) :
	running_sum = 0
	total = sum(length)
	for value in length : 
		running_sum += value
		if running_sum > total/2 :
			return value
			break

#create radom sequence of random length and gc composition
#seq = mcb185.randseq(arg.size, arg.gc)
def randseq(length, gc):
	seq = ''
	for i in range(length): 
		if random.random() < gc: seq += random.choice('GC')
		else: seq += random.choice('AT')
	return seq
	
	#i = 0 
	#while running_sum < total/2 : 
	#	running_sum += length[i]
	#	i += 1
	#return length[i]

	
#ORF:
def orf(seq):
#find ATG
	lengths = []
	for i in range(len(seq) -2): #all the starting positions we could possibly have
		start = None
		stop = None
		if seq[i:i+3] == 'ATG':
			start = i
	#one you find an ATG, you have to go by triplets
			for j in range(i, len(seq) -2, 3): #starting at A, through the rest
				codon = seq[j: j+3] # stop codon starts at j
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA' :
					stop = j
					break
		if stop != None: lengths.append((stop - start)//3) #
	return lengths




def longest_orf(seq):
	assert(len(seq) >0)

	atgs = []#find starts
	for i in range(len(seq) -2): #all the starting positions we could possibly have
		if seq[i:i+3] == 'ATG': atgs.append(i)#run through all ATGs until we hit stop codon
	max_len = 0
	max_seq = None
	for atg in atgs:
		stop = None #run right through like a train; go through each ATG
		for i in range(atg, len(seq) - 2, 3): #running through each atg letter by letter till end of seq. by 3
			codon = seq[i:i+3]
			if codon == 'TAA' or codon  == 'TAG' or codon == 'TGA': #stop codon; then compare all of them
				stop = i # letter that begins stop codon
				break #breaks the loop 
		if stop != None: 
			codingsequence_len = stop - atg + 3
			if codingsequence_len > max_len: #compares size to whats the greatest; 
				max_len = codingsequence_len #sets new coding seq to greatest
				max_seq = seq[atg:atg+codingsequence_len] # Maximum sequence is set when previously set to none ;new king
	if max_seq == None: return None #Think about it if there's a start and stop codon. Nothing to return. No sequence
	return translate(max_seq)#directly shunt to translate sequence

#translate dictionary
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}



#reverse complement
def rc_dna(dna):
	rc_dna = ''
	for i in range(len(dna) -1, -1, -1):
		nt = dna[i]
		if   nt == 'A' : rc_dna += 'T'
		elif nt == 'T' : rc_dna += 'A'
		elif nt == 'C' : rc_dna += 'G'
		elif nt == 'G' : rc_dna += 'C'
		else		   : rc_dna += 'N'
	return rc_dna

#translate
def translate(seq):
	seq = seq.upper() #normalize upper and lowercase letters. 
	protein = ''
	for i in range(0, len(seq) -2, 3): #each codon
		#protein += gcode[seq[i:i+3]]
		codon = seq[i:i+3]
		#aa = gcode[codon]
		#protein += aa
		if codon in gcode:
			protein += gcode[codon] #if codon in dict. , use it
		else: 
			protein += 'X' #any weird codon will become an X
	return protein  



