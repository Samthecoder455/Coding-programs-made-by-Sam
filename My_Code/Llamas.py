from itertools import repeat
import time

#To DO: Prompt for start size and end size
while True:
    startsize = int(input("Start size: "))

    if startsize < 9:
        print("Please try again")
    else:
        break

while True:
    endsize = int(input("End size: "))

    if endsize < startsize:
        print("Please try again")
    else:
        break

# To DO: Calculate number of years until we reach threshold
year=0
print("Populations: ", startsize, "years: ", year)

born=startsize//3
passaway=startsize//4
total = (startsize + (born) - (passaway))
year=year+1
print("Populations: ", total, "years: ", year)

new_born=total//3
new_passaway=total//4
new_result=new_born - new_passaway
new_total= total + new_result
year=year+1
print("Populations: ", new_total, "years: ", year)

for n in range (1):
    if startsize < endsize or startsize != endsize:
        new_born=new_total//3
        new_passaway=new_total//4
        new_result=new_born - new_passaway
        new_total = new_total + new_result
        year=year+1
        print("Populations: ", new_total, "years: ", year)
    if startsize > endsize or startsize == endsize:
        print(year)


# for n in range (3):
#     new_born=new_total//3
#     new_passaway=new_total//4
#     new_result=new_born - new_passaway
#     new_total = new_total + new_result
#     year=year+1
#     print("Populations: ", new_total, "years: ", year)



















    




 


        





# To DO: Print number of years