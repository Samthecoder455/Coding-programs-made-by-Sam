import cs50
while True:
    height = cs50.get_int("Height: ")
    if height >= 1 and height <= 8:
        break

dots=" "
counter_dots=" "
Ast="#"
counter_ast="#"
row=0

for l in range (height):
    number=row
    row_dots=(height-1)-number
    row_ast=number+1
    ast=counter_ast*row_ast
    dots=counter_dots*row_dots
    print(f"{dots}{ast}")
    row=row+1