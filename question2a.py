# WAP to accept a number ‘n’ and Check if ’n’ is prime

try:
    n=int(input("Enter a number : "))
    if n<=1:
        print(f"{n} is not prime number.")
    else:
        count=0 
        for i in range(2,n//2+1):
            if n%i==0:
                count+=1
        if count>0:
            print(f"{n} is not prime number.")
        else:
            print(f"{n} is prime number.")
                    
except ValueError:
    print("Please input valid number.")