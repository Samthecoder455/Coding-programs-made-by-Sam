Weight=float(input("Weight: "))
Kg_or_pounds=input("(K)g or (L)bs: ")
    
if Kg_or_pounds == "L" or Kg_or_pounds == "l":
    print("Your Weight in Kilograms is",Weight*0.45)

elif Kg_or_pounds == "K" or Kg_or_pounds == "k":
    print("Your Weight in pounds is",Weight*2.20)

else:
    print("Please type K for Kilograms or L for Pounds")

