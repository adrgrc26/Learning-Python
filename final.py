#Complexity Filter
##input genomic data; output masked version where low-complexity regions are replaced either with an ambuguity character (N = nt, X = aa) or lowercase.
### nt or aa sequence and have separate default thresholds for each
## output = lowercase, N, or X
import argparse
import math
import mcb185
import os


#pulling fasta files; setting window; threshold; entropy is different(nt=4/aa=20)
parser = argparse.ArgumentParser(description='Compute complexity filter.')
parser.add_argument('--fasta', required=True, type=str,
	metavar= '<str>', help='input a sequence file')

parser.add_argument('--w', required=False, type=int, default=10,
	metavar='<int>', help='window for complexity (AA) [%(default)i]')


parser.add_argument('--t1', required=False, type=float, default=1.0,
	metavar='<float>', help= 'default threshold for nts [%(default).3f]')
parser.add_argument('--t2', required=False, type=float, default=2.5,
	metavar='<float>', help= 'default threshold for AAs [%(default).3f]')

#switch default aa and nt

parser.add_argument('--nt', action='store_true',
	help='on= you are inputing a nt seq, off = file has AAseq')
parser.add_argument('--lc', action='store_true',
	help='on= receive output withlowercase, off = receive output with N or X')
#finalization
arg = parser.parse_args()






#this ensures that fasta file > 0
filesize = os.path.getsize(arg.fasta)
if filesize == 0:
	print("The file is empty")


#read the fasta file in AAs
if arg.fasta.endswith('.fa'): # dumbpproof 1/4
	for name, seq in mcb185.read_fasta(arg.fasta):
		seq = seq.upper()	#lower --> upper problem
		print(f'>{name}')
else : print('wrong file; did not provide fasta format') # dumb-proof 2/4


#setting entropy
def entropy(probs):
	assert(math.isclose(sum(probs), 1.0))
	h = 0
	for p in probs:
			if p != 0: h -= p * math.log2(p)
	return h
#protect your program from inputs
#Challenges/code
#idiot proof:  unexpected(hopefully ; what would you do with the sequence of the wrong letters; try to put a microsoft word? Error. lowercase? Almost correct; )

def nt_seq_entropy(seq):
		A = 0
		T = 0
		C = 0
		G = 0
		total = 0
		for nt in seq:
			total += 1
			if		nt == 'A'	:	A += 1
			elif nt == 'T' : T += 1
			elif nt == 'C' : C += 1
			elif nt == 'G' : G += 1
			else : total -= 1
		if total != 0:
			A /= total
			T /= total
			C /= total
			G /= total
			return entropy((A, T, C, G))
		else :
				return 0


def aa_seq_entropy(seq):
		A = 0
		C = 0
		D = 0
		E = 0
		F = 0
		G = 0 
		H = 0
		I = 0
		K = 0
		L = 0
		M = 0
		N = 0
		P = 0
		Q = 0
		R = 0
		S = 0
		T = 0
		V = 0
		W = 0
		Y = 0
		tot = 0
		for aa in seq:
			tot += 1
			if		aa == 'A' : A += 1
			elif aa == 'C' : C += 1
			elif aa == 'D' : D += 1
			elif aa == 'E' : E += 1
			elif aa == 'F' : F += 1
			elif aa == 'G' : G += 1
			elif aa == 'H' : H += 1
			elif aa == 'I' : I += 1
			elif aa == 'K' : K += 1
			elif aa == 'L' : L += 1
			elif aa == 'M' : M += 1
			elif aa == 'N' : N += 1
			elif aa == 'Q' : Q += 1
			elif aa == 'R' : R += 1
			elif aa == 'S' : S += 1
			elif aa == 'T' : T += 1
			elif aa == 'V' : V += 1
			elif aa == 'W' : W += 1
			elif aa == 'Y' : Y += 1
			else : tot-=1 
		if tot != 0:
			A/=tot
			C/=tot
			D/=tot
			E/=tot
			F/=tot
			G/=tot
			H/=tot
			I/=tot
			K/=tot
			L/=tot
			M/=tot
			N/=tot
			P/=tot
			Q/=tot
			R/=tot
			S/=tot
			T/=tot
			V/=tot
			W/=tot
			Y/=tot
			return entropy((A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y))
		else: return 0


	
# look through protein
out = ''
w = arg.w
t = None
r = None
f = None #store fxn in variable
#t1 = arg.t1 #nt
#t2 = arg.t2 #aa


if arg.nt:
	t = arg.t1
	r = 'N'
	f = nt_seq_entropy
else:
	t = arg.t2
	r = 'X'
	f = aa_seq_entropy

for i in range(len(seq)-w+1):
	wind = seq[i:i+w]
	h = f(wind)
	if h>=t: out+= seq[i]
	elif arg.lc: out += seq[i].lower()
	else:	out += r #if user didn't put lc, they want N
print(out)



"""

Final project : WORKED WITH VICTORIA REES!!!!

THANKS FOR THE QUARTER IAN!

"""
##made a swtich to type in . Turn switch on . 
#in our amino acid sequences. we're ever getting a lowercase letter. where are the lower coplexion sections? 
#m is not the best way to differentiate between 
