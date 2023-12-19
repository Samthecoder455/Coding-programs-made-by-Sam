import random
list_same_num=[]
user_guess_list_new=[]        
c4=0
c5=0
list_pico=[]
c3=0
c=0
c1=0
c2=0
counter_3=0
pico=0
fermi_list=[]
counti=0
counter=0
fermi_check=[]
random_number_list_new=[]
random_number=random.randint(100,999)
attempt_counter_og=10
attempt_counter=attempt_counter_og
while counti == 0:
    random_number=str(random_number)
    random_number_list=list(random_number)
    random_number_list_new=[]#this is important
    for z in random_number_list:
        j=int(z)
        random_number_list_new.append(j)
    random_number_list_check=list(set(random_number_list_new))
    if len(random_number_list_check) < 3:
        random_number=random.randint(100,999)
        print(random_number)
    if len(random_number_list_check) == 3:
        break
while True:
    if counti == 1 or counti > 1:
        counter=counter+1
        counter_3=counter
    if counti >= 1 and counter == 1:
        random_number=random.randint(100,999)
    while counti >= 1 and counter == 1:
        random_number=str(random_number)
        random_number_list=list(random_number)
        random_number_list_new=[]#this is important
        for z in random_number_list:
            j=int(z)
            random_number_list_new.append(j)
        random_number_list_check=list(set(random_number_list_new))
        if len(random_number_list_check) < 3:
            random_number=random.randint(100,999)
        if len(random_number_list_check) == 3:
            break
    if counti == 0:
        counter_3=counter_3+1
    if counter_3 == 11:#guess number is exclusive
        print("Out of guess attempts, the number was", (random_number))
        break
    if counter_3 > 1 or counti >= 1:
        user_guess_list_new=[]
        list_same_num=[]
        fermi_list=[]
        fermi_check=[]
        list_pico=[]
        c3=0
        c2=0
        c4=0
        c5=0
    user_guess=int(input("guess the number: "))
    user_guess_str=str(user_guess)
    if len(user_guess_str) < 3:
        print("The number you entered is not three digits! Please try again ")
        break
    if counti >= 1 and counter_3 == 1:
        attempt_counter=attempt_counter_og
    user_guess_list=list(user_guess_str)
    for k in user_guess_list:
        m=int(k)
        user_guess_list_new.append(m)
    list_add=random_number_list_new+user_guess_list_new
    for m in range (len(list_add)):
        count_occur=list_add.count(list_add[c3])
        if count_occur > 1:
            list_same_num.append(list_add[c3])
        c3=c3+1
    list_same_num=list(set(list_same_num))
    #fermi
    for _ in range (3):
        if random_number_list_new[c] == user_guess_list_new[c]:
            fermi_list.append(random_number_list_new[c])
            c=c+1
            if c == 3:#becuase the numbers are 3 digits only so the most the list has is 3 elements
                c=0
                break
        elif random_number_list_new[c] != user_guess_list_new[c]:
            c=c+1
            if c == 3:
                c=0
                break
    #pico
    list_pico=list_same_num
    for q in fermi_list:
        p=q
        fermi_check.append(p)
    for _ in range (len(fermi_list)*len(list_same_num)):
        if len(fermi_list) == 1:
            if fermi_list[c1] == list_pico[c2]:
                list_pico.pop(c2)
                if len(list_pico) == len(list_same_num)-1:
                    break
            elif fermi_list[c1] != list_pico[c2]:
                if len(list_pico) != len(list_same_num)-1:
                    c2=c2+1
    for _ in range (len(fermi_list)*len(list_same_num)):
        if len(fermi_check) == 2:
            if fermi_check[c4] == list_pico[c5]:
                fermi_check.pop(c4)
                list_pico.pop(c5)
            elif fermi_check[c4] != list_pico[c5]:
                c4=c4+1
        if len(fermi_check) == 1 and len(list_pico) == 1:
                c4=0
                if fermi_check[c4] == list_pico[c5]:
                    fermi_check.pop(c4)
                    list_pico.pop(c5)
                    if len(list_pico)== 0 and len(fermi_check) == 0:
                        break
    while True:
        if len(fermi_list) == 3:
            list_pico=[]
            break
        else:
            break
    #bagels
    for a in range (1):
        if len(list_pico) == 0 and len(fermi_list) == 0:
            if len(fermi_list) == 3:
                    break
            print("Bagels")  
        if len(list_pico) == 0:
            pico=0
            if len(fermi_list) == 3:
                    break
            print("Pico, None")
        if len(fermi_list) == 0:
            if len(fermi_list) == 3:
                    break
            print("Fermi, None")
        if len(fermi_list) > 0:
            for q in fermi_list:
                if len(fermi_list) == 3:
                    break
                print("Fermi",q)
        if len(list_pico) > 0:
            for l in list_pico:
                if len(fermi_list) == 3:
                    break
                print("Pico", l)
        if attempt_counter != 0:
            attempt_counter=attempt_counter-1
            print("You have",attempt_counter , "attempts left")
    if len(fermi_list) == 3:
        print("You got the number!")
        ask_user=str(input("Would you like to play again? (yes/no) "))
        if ask_user == "yes":
            counti=counti+1
            counter=0
            pass
        elif ask_user == "no":
            print("Thanks for playing!")
            break
