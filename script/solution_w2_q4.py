'''
Week2 - compute hamming distance
'''

##with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\data\week_2_q3.txt') as input_data:
##    seqA,seqB = [v.strip() for v in (input_data.readlines())]

pattern='ATTCTGGA'
seq='CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
itr = len(seq)/len(pattern)

for i in range(itr):
    if seq[i:i+itr] == pattern
distance = 0
for i in xrange(len(seqA)):
    if seqA[i] != seqB[i]:
        distance +=1
        
with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\output\sol_w2_q4.txt','w') as out_data:
    out_data.write(str(distance))


