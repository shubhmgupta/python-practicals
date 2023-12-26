# Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to Print half the values of the tuple in one line and the other half in the next line
t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
index=len(t1)//2
for i in t1[:index]:
    print(i,end=" ")
print()
for i in t1[index:]:
    print(i,end=" ")