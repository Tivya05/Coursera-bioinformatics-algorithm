# get a list of kmers and compare it with the seq -- time expensive
# instead for each kmer in the seq, get the neighbors with the mismatches and then count the ocurrences.
# - check to see if you can count the occurences in the funtion * instead of for loop at the end**s
import time
start = time.clock()

final= []
# *
def stringNeighbors(st, alph, edits):
    ''' Given a string, an alphabet, and a maximum edit or Hamming
        distance, return all strings within that distance. '''
    
    ret = set()
    def editNeighborsHelp(st, edits, ii):
        #print "called with " + st
        #print st,edits,ii
        for i in xrange(ii, len(st)):
         #   print i
            if edits > 0:
                # Mismatch at position i
                for a in alph:
                    if a != st[i]:
                        newst = st[:i] + a + st[i+1:]
                        editNeighborsHelp(newst, edits - 1, ii+1)
       # if edits > 0:
            # Insertion just after last position
           # for a in alph: ret.append(st + a)
        ret.add(st)
        #print "result is " + str(ret)
    editNeighborsHelp(st, edits, 0)
    return ret
##n= stringNeighbors('ACGT', 'ACGT', 1)
##    with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\data\week_2_q7.txt') as input_data:
##        seq, [kmer,mismatch]=[v.strip() if ix == 0  else map(int,v.split()) for ix,v in enumerate (input_data.readlines())]

from collections import defaultdict
d=defaultdict(int)
seq='CGTCACTTCGTCCTCCCTCCCTCCCGCTCGCTCTCCACTTCTCCCTCCACTTACTTCTCCCTCCATACTCCCGCTCGCTCGCTACTTCTCCCGTCATAACTTCGCTCTCCCGCTCTCCCTCCCGCTACTTCGTCCTCCATACGCTATACGTCATACTCCACTTCTCCATACGCTATAATACTCCATACGCTACTTCGTCATAATAACTTCGTCCTCCATAACTTCGTCCGTCCTCCCGTCCGCTATACGTCCTCCACTTCTCCCGTCCGTCACTTCTCCCGCTCGCTCGCTCGTCCGCTCGCTCTCCCTCCACTTCTCCATACTCCCGCTCGCTCGTCCGCTCGTCATAACTTCGTCCTCC'
kmer=7
mismatch = 3
ham=defaultdict(int)

# get disinct k length seguences from the genome to avoid repetition
l=set()
for i in range(len(seq)-kmer+1):
	l.add(seq[i:i+kmer])
# get the neighbors instead of generating all the kmers
for e in l:
    n= stringNeighbors(e, 'ACGT', mismatch)
    final.append(n)
# get distinct kmers
kmers=set([y for x in final for y in x])
print kmers
#get the count 
#**
for v in kmers:
    for h in range(len(seq)-kmer+1):
        distance = 0
        seqA = seq[h:kmer+h]
        for j in xrange(kmer):
            if seqA[j] != v[j]:
                distance += 1
        if distance <= mismatch:
            d[v] += 1 
            ham[v]=distance
  
max_value=max(d.values())
li=[key for key,val in d.iteritems() if val == max_value]
with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\output\sol_w2_q6._pt2txt','w') as out_data:
    out_data.write(str(li))
