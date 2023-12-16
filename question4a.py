# WAP that accepts a character and print whether the character is a letter or numeric digit or a special character. 

char=input("Enter characters : ")
if char.isalpha():
    print("Letter")
elif char.isdigit():
    print("Numeric digit")
else:
    print("Special Character")