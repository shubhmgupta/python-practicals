# Write a function that accepts two strings and returns the indices of all the occurrences of
# the second string in the first string as a list. If the second string is not present in the first
# string then it should return -1. 

str1=input("Enter first sentence : ")
str2=input("Enter second sentence : ")
list=[]
str2_dict={str2[i]:i for i in range(len(str2))}
str1_dict={j:str1[j] for j in range(len(str1))}
for i in str2_dict.keys():
    if i in str1:
        for key,values in str1_dict.items():
            if values==i:
                list.append(key)
    else:
        list.append(-1)
print(list)