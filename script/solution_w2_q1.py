'''
Week2 - compute skew diagram list
replication starts at forward strand and then the reverse strand
gc count decreases in reverse strand and starts to increase after the ori region
index 0=0
'''

with open('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\data\week_2_q1.txt') as input_data:
    genome = input_data.read()


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
   
# print ' '.join(str(i) for i in l) 


with open ('C:\Users\callk_000\Documents\coursera\Coursera-bioinformatics-algorithm\output\sol_w2_q1.txt','w') as out_data:
    out_data.write(' '.join(str(i)for i in l))


