'''
Week2 - Find the most frequent k-mers with mismatches in a string
 ACGTTGCATGTCGCATGATGCATGAGAGCT
     4 1

Sample Output:
     GATG ATGC ATGT
'''

##with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\data\week_2_q6.txt') as input_data:
##    genome, [kmer,mismatch]=[v.strip() if ix == 0  else map(int,v.split()) for ix,v in enumerate (input_data.readlines())]


from collections import defaultdict
from itertools import product
kmer=3
genome='ACG'
mis=2
distance=0
l = []
d=defaultdict(int)
ham=defaultdict(int)
bases='ATGC'
s=[''.join(p) for p in product(bases, repeat=mis)]

#s = {genome[i:kmer+i] for i in range(len(pattern)-kmer+1)}
##s=[''.join(p) for p in product(bases, repeat=kmer)]

print s
for m in range(len(genome)-kmer+1):
    pattern = genome[m:kmer+m]
  
    for i in range(len(pattern)-mis+1):
        for j in range (len(s)):
            if i == 0:
                            l.append(pattern.replace(pattern[0:mis],s[j]))
                            
            else:
                            l.append( pattern[:i]+s[j]+pattern[i+mis:])
                            
se=set(l)
for v in se:
    for h in range(len(genome)-kmer+1):
        distance = 0
        seqA = genome[h:kmer+h]
        for j in xrange(kmer):
            if seqA[j] != v[j]:
                distance += 1
        if distance <= mis:
            d[v] += 1 
            ham[v]=distance

    
max_value=max(d.values())
li=[key for key,val in d.iteritems() if val == max_value]

print li
##print ' '.join(str(i) for i in l) 
    


with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\output\sol_w2_q5.txt','w') as out_data:
    out_data.write(' '.join(str(i) for i in l) )


