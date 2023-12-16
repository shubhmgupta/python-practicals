# WAP to create a pyramid of the character ‘*’

try:
    n=int(input("Enter a number : "))
    for i in range(1,n):
        spaces=' '*(n-i)
        stars='*'*(2*i-1)
        print(spaces+stars)
except ValueError:
    print("Please input number")