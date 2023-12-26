# Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Print another tuple whose values are even numbers in the given tuple. 
t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2=tuple(i for i in t1 if i%2==0)
print(t2)