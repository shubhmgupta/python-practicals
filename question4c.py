# WAP that accepts a character and if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE)

char=input("Enter a character : ")
if char.isdigit():
    l=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
    if int(char) >=0 and int(char) <=9:
        print(f"{char} = {l[int(char)]}")
    else:
        print("Number is either less than 0 or greater than 9")
else:
    print(f"{char} is not digit.")