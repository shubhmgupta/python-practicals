# WAP to Replace a character by another character in a string.
str=input("Enter Sentence : ")
rep=input("Enter character to replace : ")
repwith=input("Enter charater to replace with : ")
replaced=""
for i in str:
    if i==rep:
        replaced+=repwith
    else:
        replaced+=i
print(f"Original : {str} ")
print(f"Final : {replaced} ")