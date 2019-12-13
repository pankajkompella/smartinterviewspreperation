a=int(input())
n=int(input())
ans=1
x=a
while n!=0:
    if (n&1)==1:
        ans=ans*x
    x=x*x
    n=n>>1
print(ans)
