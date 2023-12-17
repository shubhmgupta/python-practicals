# WAP to swap the first n characters of two strings.

str1=input("Enter first Sentence : ")
str2=input("Enter Second Sentence : ")
n=int(input("Enter value of n to swap : "))
if n> min(len(str1),len(str2)):
    print("cannot Swap")
else:
    new_str1=str2[:n]+str1[n:]
    new_str2=str1[:n]+str2[n:]
print(f"First swapped : '{new_str1}'")
print(f"Second swapped : '{new_str2}'")
