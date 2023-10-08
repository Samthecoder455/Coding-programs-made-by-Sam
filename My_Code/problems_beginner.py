#Excercise 1: Given two integer numbers, 
#return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a=int(input("Give me the first integer:  "))
b=int(input("Give me the second integer: "))

product=a*b
sum=a+b

if product == 1000 or product < 1000:
    print(product)
elif product != 1000 or product < 1000:
    print(sum)