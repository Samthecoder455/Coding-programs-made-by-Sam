sum_ans=0
sum_sec=0
sumi=0
k=0
for n in range (3,1000,3):
    sum_ans=sum_ans+n

for l in range (5,1000,5):
    if l % 3 == 0:
        k=l
        sumi=sumi+k
    sum_sec=sum_sec+l
jim=sum_sec-sumi

for n in range (1):
    sum_final=sum_ans+jim
    print(sum_final)
 

    