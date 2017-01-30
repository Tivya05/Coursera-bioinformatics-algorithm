

'''
Clump Finding Problem: Find patterns forming clumps in a string.
Input: A string Genome, and integers k, L, and t.
Output: All distinct k-mers forming (L, t)-clumps in Genome.
'''

# slide through the genome with window size of k and add to the dictionary
# if count of the key (seq) is = t then compare the index and check if it is a cluster

from collections import defaultdict()
d = defaultdict(list)
count = defaultdict()
def Clumpfind (genome, k, l, t):
for i in xrange (len(genome)-k+1):
		g=genome[i:k+i]
		d[g].append(i+k)  
		if len(d[g])== t:
			if abs((d[g][0]-k)-(i+k))<l:
				count[g]=1
				del d[g][0]
			else:
				del d [g][0]
	return len(count)

# read the input file (Ecoli genome) and run the fucntion
with  open(‘E_coli.txt’) in_data:
	genome, k,l,t= [line.strip() if  ix == 0 else map(int,line.split()) for ix,line in enumerate(in_data.readlines())]
clumpfind(genome,k,l,t)
print “total numbers of kmers %d” len(count)s

#  send the output to coursera format
With open(‘week1_clumpfind.txt’,’w’) as out_file:
