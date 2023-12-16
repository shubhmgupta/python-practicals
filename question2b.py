#WAP to accept a number ‘n’ and Generate all prime numbers till ‘n’

def CheckPrime(n):
    if n<=1:
        return False
    else:
        count=0
        for i in range(2,n//2+1):
            if n%i==0:
                count+=1
        if count>0:
            return False
        else:
            return True
try:
    prime=[]
    n=int(input("Enter Number : "))
    for i in range(1,n+1):
        if CheckPrime(i):
            prime.append(i)
    print(f"Prime numbers are till {n} are {prime}")
except ValueError:
    print("Invalid input")