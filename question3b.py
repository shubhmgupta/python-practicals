# WAP to create a reverse pyramid of the character ‘*’

try:
    n=int(input("Enter a number : "))
    for i in range(n,-1,-1):
        spaces=' '*(n-i)
        stars='*'*(2*i-1)
        print(spaces+stars)
except ValueError:
    print("Please input number")