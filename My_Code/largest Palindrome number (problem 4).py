while True:
    n_ask=int(input("Give me the number of digits the starting and ending digits should be: "))
    if n_ask <= 1:
        print("the digit number should be above 1")
    if n_ask > 1:
        break
zeros=(n_ask-1) * "0"
final_zero = "1" + zeros
n1=int(final_zero)
numb=n1
n2=int(final_zero)
n_final=0
z=0
list_reverse=[]
list_reverse_2=[]
list_final_pali=[]
while True:
    #multiplication
    n_final=n1*n2
    n_final_str=str(n_final)
    len_n_final=len(n_final_str)
    #check if it's a palindrome
    conver_final=n_final
    for n in range (len_n_final):
        dig=conver_final%10
        list_reverse.append(dig)
        conver_final=conver_final//10
    list_reverse_2=list_reverse
    list_reverse=[]
    z=0
    for k in list_reverse_2:
        z=z+k
        z=z*10
    z=z//10
    #compare and add to list
    if z == n_final:
        list_final_pali.append(n_final)
        n1=n1+1
    elif z != n_final:
        n1=n1+1
    if n1 == (numb*10):
        n1=numb
        n2=n2+1
    if n2 == (numb*10):
        break
set_num=set(list_final_pali)#convert to set to remove duplicate elements in list
list_num=list(set_num)#convert the set back to list
final_list=sorted(list_num)#use in built sort function to sort elements from asending order and store in new list
print(f"the largest palindrome made from the product of two {n_ask} digit numbers is {final_list[-1]}")
