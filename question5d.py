# WAP to Remove all occurrences of a character from a string. 

str=input("Enter sentence : ")
char=input("Enter character to remove : ")
new_str=''
for i in str:
    if i==char:
        new_str+=''
    else:
        new_str+=i
print(f"Original : {str}")
print(f"Final : {new_str}")