# WAP to accept a number ‘n’ and Generate first ‘n’ prime numbers

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
    num=1
    while len(prime)<n:
        if CheckPrime(num):
            prime.append(num)
        num+=1
    print(f"First {n} prime numbers are {prime}")
except ValueError:
    print("Invalid input")