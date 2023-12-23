# WAP to create a list of the cubes of only the even integers appearing in the input list (may have elements of other types also) using for loop 
n=eval(input("Enter values sep by comma : "))
list1=[]
for i in n:
    if type(i)==int and i%2==0:
        list1.append(i**3)
print(list1)
