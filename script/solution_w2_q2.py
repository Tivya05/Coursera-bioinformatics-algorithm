'''
Week2 - compute min skew value to find approximate ori location
'''
import numpy as np
with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\data\week2_q2.txt') as input_data:
    gen = [v.strip() for i,v in enumerate(input_data.readlines()) if i==0]

genome=gen[0]
l=[0]*(len(genome)+1)
min_value=0
min_index=[]

for i in xrange(len(genome)):
    if genome[i] == 'C':
        l[i+1] = l[i]-1
    elif genome[i] == 'G':
            l[i+1] = l[i]+1
    else:
        l[i+1]=l[i]

        
skew_points= np.array(l)
sol=np.where(skew_points == min(l))

with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\output\sol_w2_q2.txt','w') as out_data:
    out_data.write(' '.join(map(str,sol)).strip('[]'))


