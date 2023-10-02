# TODO
import cs50

while True:
    height = cs50.get_int("Height: ")
    if height >= 1 and height <= 8:
        break

dots = " "
counter_dots = " "
Ast = "#"
counter_ast = "#"
row = 0
row_1 = 0

for l in range(height):
    number = row
    row_dots = (height - 1) - number
    row_ast = number + 1
    row_1 = row_1 + 1
    ast = counter_ast * row_ast
    ast_1 = Ast * row_1
    dots = counter_dots * row_dots
    print(f"{dots}{ast}  {ast_1}")
    row = row + 1
