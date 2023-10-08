num1=1
num2=2
list_terms=[num1, num2]
num_stop=4000000
while True:
    numx=list_terms[-1]+list_terms[-2]
    list_terms.append(numx)
    if numx > num_stop:
        list_terms.remove(numx)
        break
list_even=[]
for x in list_terms:
    if x % 2 == 0:
        list_even.append(x)

sum_1=list_even[0]+list_even[1]
n=2
sum=0
while True:
    sum=sum_1+list_even[n]
    sum_1=sum
    n=n+1
    if n == len(list_even)-1:
        sum=sum_1+list_even[n]
        break
print(sum)