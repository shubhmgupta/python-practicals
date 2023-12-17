# WAP to Find the frequency of a character in a string. 

str=input("Enter sentence : ")
char=input("Enter Char to find frequency : ")
frequency=0
for i in str:
    if i==char:
        frequency+=1
print(f"Frequency of {char} in '{str}' is {frequency}")