#ask user for string and .lower() turns return value to lowercase
string=input("Give a String: ").lower()
reverse = string[::-1]
reverse = reverse.lower()
print(reverse)
if reverse == string:
    print("This text you provided is a palindrome")
else:
    print("This text is not a palindrome")
    
