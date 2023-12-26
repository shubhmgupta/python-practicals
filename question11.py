# Write a function that prints a dictionary where the keys are numbers between 1 and 5
# and the values are cubes of the keys
n=int(input("Enter a number : "))
def Cubes(n):
    dict={i:i**3 for i in range(1,n+1)}
    print(dict)
Cubes(n)