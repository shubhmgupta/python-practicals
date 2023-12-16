# WAP that accepts a character and if the character is a letter, print whether the letter is uppercase or lowercase

char=input("Enter characters : ")
if char.isalpha():
    if char.islower():
        print("Lowercase Letter")
    else:
        print("Uppercase Letter")
elif char.isdigit():
    print("Numeric digit")
else:
    print("Special Character")