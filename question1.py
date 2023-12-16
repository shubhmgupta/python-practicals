# WAP to find the roots of a quadratic equation with error handling

import math
try:
    a=int(input("Enter value of a : "))
    b=int(input("Enter value of b : "))
    c=int(input("Enter value of c : "))
    D=b**2-4*a*c
    if D>=0:
        root1=-b+math.sqrt(D)
        root2=-b-math.sqrt(D)
        print(f"Roots of equation are {root1} and {root2}")
    else:
        print("No real root exist.")
except ValueError:
    print("Please input valid number.")