'''
Week2 - compute hamming distance
'''

with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\data\week_2_q4.txt') as input_data:
    pattern,seq,limit = [v.strip() for v in (input_data.readlines())]
print pattern
print limit
##pattern='ATTCTGGA'
##seq='CGCCCGAATCCAGAACGCATTCCCA'


itr=len(pattern)
print itr
distance = 0
l=[]

for i in range(len(seq)-len(pattern)+1):
    seqA=seq[i:itr+i]
    distance = 0
    
    for j in xrange(len(pattern)):
        if seqA[j] != pattern[j]:
            distance +=1
    if distance <= int(limit):
        l.append(i)
#print ' '.join(map(str,l))
      
with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\output\sol_w2_q4.txt','w') as out_data:
    out_data.write(' '.join(map(str,l)))


