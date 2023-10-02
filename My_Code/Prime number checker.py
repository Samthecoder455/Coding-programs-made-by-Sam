ask_prime=int(input("Give me a number from 1-100: "))
prime_list=[2,3,5,7,11,13]
for n in range (1):
    if ask_prime in prime_list:
        print("The number you provided is a prime number")
        break
    Sam = ask_prime % 2
    if Sam == 0: #2
        print("The number you provided is not a prime number")
    elif Sam != 0:
        Sam = ask_prime % 3  #3
        if Sam == 0:
            print("The number you provided is not a prime number")
        elif Sam != 0:
            Sam = ask_prime % 5  #5
            if Sam == 0:
                print("The number you provided is not a prime number")
            elif Sam != 0:
                Sam = ask_prime % 7 #7
                if Sam == 0:
                    print("The number you provided is not a prime number")
                elif Sam != 0:
                    Sam = ask_prime % 11 #11
                    if Sam == 0:
                        print("The number you provided is not a prime number")
                    elif Sam != 0:
                        Sam = ask_prime % 13 #13
                        if Sam == 0:
                            print("The number is you provided is not a prime number")
                        elif Sam != 0:
                            print("The number you provided is a prime number")


                
                        




    

        
    


    
    



    

