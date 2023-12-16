# WAP to find the roots of a quadratic equation with error handling

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