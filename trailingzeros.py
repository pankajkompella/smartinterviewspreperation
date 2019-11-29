"""program to find number of trailing zeros in factorial of given number:
https://www.purplemath.com/modules/factzero.htm"""


t=int(input())
for _ in range(t):
    n=int(input())
    i=5
    p=0
    while n//i!=0:
        p+=n//i
        i*=5
    print(p)

    
