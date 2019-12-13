#divisors of a number n
import math
n=int(input())
c=0
for i in range(1,int(math.sqrt(n))):
    if n%i==0:
        c+=2
if n%2==0:
    print(c-1)
else:
    print(c)
