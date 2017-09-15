'''
Week2 - Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches.
For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 
'''

with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\data\week_2_q5.txt') as input_data:
    pattern,seq,mismatch = [v.strip() for v in (input_data.readlines())]

print pattern,mismatch
##pattern='GAGG'
##seq='TTTAGAGCCTTCAGAGG'
##mismatch=2


itr=len(pattern)
distance = 0
count=0

for i in range(len(seq)-itr+1):
    seqA=seq[i:itr+i]
    distance = 0
        
    for j in xrange(len(pattern)):
        if seqA[j] != pattern[j]:
            distance +=1
    if distance <= int(mismatch):
        count += 1
print count
       
with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\output\sol_w2_q5.txt','w') as out_data:
    out_data.write(str(count))


