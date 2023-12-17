# WAP to Remove the first occurrence of a character from a string.

str=input("Enter Sentence : ")
char=input("Enter character to remove : ")
index=str.find(char)
if index !=-1:
    new_str=str[:index]+str[index+1:]
    print(f"Original : {str}")
    print(f"Final : {new_str}")
else:
    print(f"'{char}' not in '{str}' ")