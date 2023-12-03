#Excercise 1: Given two integer numbers, 
#return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# a=int(input("Give me the first integer:  "))
# b=int(input("Give me the second integer: "))

# product=a*b
# sum=a+b

# if product == 1000 or product < 1000:
#     print(product)
# elif product != 1000 or product < 1000:
#     print(sum)


# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# print("Printing current and previous number sum in a range(10)")
# current_number=0
# previous_number=0
# sum_num=0
# for n in range (1,11,1):
#     print(f"Current Number {current_number} Previous Number {previous_number} Sum: {sum_num}")
#     current_number=current_number+1
#     previous_number=current_number-1
#     sum_num=current_number+previous_number

# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# ask_string=str(input("Give me a string: "))

# counter_index=0
# list_char=[]
# print(f"Original string {ask_string}")
# print(f"Printing only even index chars")
# for m in range (len(ask_string)):
#     list_char.append(ask_string[counter_index])
#     counter_index=counter_index+2
#     if counter_index == len(ask_string):
#         for x in list_char:
#             print(x)
#         break
#     if counter_index == len(ask_string)-1:
#         list_char.append(ask_string[counter_index])
#         for j in list_char:
#             print(j)
#         break

# Exercise 4: Remove first n characters from a string.
# print("Removing charecters from string")
# def remove_chars(text, num):
#     print(f"orignial string: {text}")
#     removed_text=text[0:num] #could've use text[num:], it would've started with num and ended with end of string.  
#     final_text=text.replace(removed_text,"") #replace the sliced text with an empty string.
#     return final_text
# print(f"the final charecters are: ", remove_chars("pynative", 2))

# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# def ask_list (number_x, number_y):
#     if number_x[0] == number_x[-1]:
#         print(f"Given list: {number_x} ")
#         print("result is True")
#     elif number_x[0] != number_x[-1]:
#         print("result is False")
    
#     if number_y[0] == number_y[-1]:
#         print(f"Given list: {number_y} ")
#         print("result is True")
#     elif number_y[0] != number_y[-1]:
#         print(f"numbers_y = {number_y}")
#         print("result is False")
#     return number_x, number_y
# ask_list([10,20,30,40,10],[75, 65, 35, 75, 30])

# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# def ask_list(list_user):
#     print(f"Given list is {list_user}")
#     print("Divisible by 5")
#     for x in list_user:
#         if x % 5 == 0:
#             print(x)
#         if x % 5 != 0: #Don't need the second if statement. 
#             continue
# ask_list([10, 20, 33, 46, 55])

# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

# list_sam=[]
# emma="Emma is good developer. Emma is a writer. Emma is Emma who is Emma's Emma."
# count=0
# count2=1
# while True:
#     sliced_object=emma[count:count2]
#     list_sam.append(sliced_object)
#     count=count+1
#     count2=count2+1
#     if count == len(emma) and count2-1 == len(emma):
#         break
# index0=0
# index1=1
# index2=2
# index3=3
# num=0
# for x in list_sam:
#     if list_sam[index0] == "E" and list_sam[index1] == "m" and list_sam[index2] == "m" and list_sam[index3] == "a":
#         num=num+1
#     index0=index0+1
#     index1=index1+1
#     index2=index2+1
#     index3=index3+1
#     if index3 == len(list_sam):
#         break
# print(f"Emma appeared {num} times")   


#Exercise 8: Print the following pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# num=1
# print(num)
# for l in range (4):
#     num=num+1
#     num_str=str(num)
#     for n in range (num):
#         print(num_str, end=" ")
#     print()#moves to new line once this loop has completed running.

# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# num=int(input("Give me a palindrome number: "))
# sam=str(num)
# bill=sam[-1::-1]
# bill=int(bill)
# if bill == num:
#     print(f"original number {num}")
#     print(f"Yes. Given number is a palindrome")
# if bill != num:
#     print(f"original number {num}")
#     print(f"No. Given number is not a palindrome")

# Exercise 10: Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list

# def func_list (l_1, l_2):
#     l_3=[]
#     for x in l_1:
#         if x % 2 != 0:
#             l_3.append(x)
#     for y in l_2:
#         if y % 2 == 0:
#             l_3.append(y)
#     return l_3
# result=func_list([10, 20, 25, 30, 35], [40, 45, 60, 75, 90])
# print(f"result list: {result}")

# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
# given_int=int(input("Give me a number: "))
# list_sam=[]
# bill=given_int
# while True: # could say while number > 0, then you can remove the if statement
#     sam=bill%10
#     list_sam.append(sam) #don't need to create a list and add to it
#     bill=bill//10 #just print sam inside the loop with print(sam, end=" ")
#     if bill == 0:
#         break
# for x in list_sam:
#     print(x, end=" ")

# Exercise 12: Calculate income tax for the given income by adhering to the rules below

# For example, suppose the taxable income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.

# num=int(input("Give me the number: ")) #make sure to add the first two if statements to handle the 10 grand and 20 grand inputs.
# for n in range (1):
#     if num <= 10000:
#         final=0 # final is 0 becuase when we do 10,000 by 0 and then divide by 100, we get 0.
#         print(f"given income: {num}")
#         print(final)
#         break
#     if num <=20000:
#         first=(10000*0)/100
#         second=10000
#         second=num-10000
#         second=(second*10)/100
#         final=first+second
#         print(f"given income: {num}")
#         print(final)
#         break

#     if num > 20000: #if it was less than 200000 then say that fidn the taxable income of the next 10,000 
#         first=10000
#         second=10000
#         rem=num-20000
#         first=(first*0)/100
#         second=(second*10)/100
#         rem=(rem*20)/100
#         final=first+second+rem
#         print(f"given income: {num}")
#         print(final)
#         break

# Exercise 13: Print multiplication table from 1 to 10

# t=1
# n=1
# for x in range (10):
#     for k in range (10):
#         f=t*n
#         print(f, end=" ")
#         t=t+1
#     print()
#     t=1
#     n=n+1
# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
# ast="*"
# n=5
# for x in range (5):
#     for l in range (n):
#         print(ast, end=" ")
#     n=n-1
#     print()

# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent (base,exp):
#     ans=base**exp #main things is here
#     print(f"base = {base}")
#     print(f"exponent = {exp}")
#     print(f"{base} raises to the power of {exp}: {ans}")
#     sam=str(f"{base} *")
#     bill=sam*exp 
#     split_2=bill[0:len(bill)-1]
#     print(f"i.e ({split_2} = {ans})")
# exponent(5,4)






    



    








    



