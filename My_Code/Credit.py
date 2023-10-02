import cs50
credit_num=cs50.get_int("Enter your credit card number: ")
list_num=[]
list_select=[]
list_select_2=[]
list_multiply=[]
cal=credit_num
while True:
    if credit_num != 0:
        sam=cal%10
        list_num.append(sam)
        cal=int(cal/10)
    if cal == 0:
        break
list_num.reverse()
bill=-2
length=len(list_num)
test=length//-1
mod=length%2
for n in range(len(list_num)):
    if mod == 0:
        sam=list_num[bill]
        list_select.append(sam)
        bill=bill-2
        if bill == -1*length:
            sam=list_num[bill]
            list_select.append(sam)
            break
    if mod != 0:
        sam=list_num[bill]
        list_select.append(sam)
        bill=bill-2
        if bill == test+1:
            sam=list_num[bill]
            list_select.append(sam)
            break
mult=2
coun=0
list_mult=[]
for x in list_select:
    coun=mult*x
    list_mult.append(coun)

list_mult_new=[]
for k in list_mult:
    j=str(k)
    list_mult_new.append(j)

num=2
jas=list_mult_new[0]+list_mult_new[1]
for m in range (len(list_mult_new)):
    if len(list_mult_new) < 2 or len(list_mult_new) == 2:
        break
    if len(list_mult_new)-1 == num:
        jas=jas+list_mult_new[num]
        break
    elif len(list_mult_new)-1 != num:
        jas=jas+list_mult_new[num]
        num=num+1

number=int(jas)


list_sep=[]
jon=number
while True:
    if number != 0:
        sam_2=jon%10
        list_sep.append(sam_2)
        jon=int(jon/10)
    if jon == 0:
        break
list_sep.reverse()

var=0
after=1
jack=0
final=0
check=list_sep[0]+list_sep[after] 
for p in range(len(list_sep)-2):
    after=after+1
    var=list_sep[after]
    jack=jack+var
final=check+jack


bill_2=-1
list_select_2=[]
length_2=len(list_num)
mod_2=length_2%2
calcu_2=(-1*length_2)+1
for l in range(len(list_num)):
    if mod_2 == 0:
        sam_2=list_num[bill_2]
        list_select_2.append(sam_2)
        bill_2=bill_2-2
        if bill_2 == calcu_2:
            sam_2=list_num[bill_2]
            list_select_2.append(sam_2)
            break
    if mod_2 != 0:
        sam_2=list_num[bill_2]
        list_select_2.append(sam_2)
        bill_2=bill_2-2
        if bill_2 == -1*length_2:
            sam_2=list_num[bill_2]
            list_select_2.append(sam_2)
            break

var_2=0
after_2=1
jack_2=0
final_2=0
check_2=list_select_2[0]+list_select_2[after_2] 
for v in range(len(list_select_2)-2):
    after_2=after_2+1
    var_2=list_select_2[after_2]
    jack_2=jack_2+var_2
final_2=check_2+jack_2
full_final=final_2+final
check_sum=full_final%10
checker_master = list_num[0] == 5 and list_num[1] == 1 or list_num[0] == 5 and list_num[1] == 2 or  list_num[0] == 5 and list_num[1] == 3 or  list_num[0] == 5 and list_num[1] == 4 or list_num[0]== 5 and list_num[1] == 5

checker_amex= list_num[0] == 3 and list_num[1] == 4 or list_num[0] == 3 and list_num[1] == 7

checker_visa = list_num[0] == 4

checker_visa_2=len(list_num) == 13 or len(list_num) == 16

check_amex_final = len(list_num) == 15 and checker_amex == True and check_sum == 0

check_master_final = len(list_num) == 16 and checker_master == True and check_sum == 0

check_visa_final = checker_visa_2 == True and checker_visa == True and check_sum == 0

for n in range (1):
    if check_amex_final == True:
        print("AMEX")
        break
    if check_master_final == True:
        print("MASTERCARD")
        break
    if check_visa_final == True:
        print("VISA")
        break
    if check_amex_final != True:
        print("INVALID")
        break
    if check_master_final != True:
        print("INVALID")
        break
    if checker_visa_2 != True:
        print("INVALID")
        break
    else:
        break

    