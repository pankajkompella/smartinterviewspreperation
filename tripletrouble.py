t=int(input())
for _ in range(t):
    ans=0
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(0,31):
        c=0
        for j in range(n):
            
            if ((l[j]>>i)&1)==1:
                c+=1
        
        if c%3!=0:
            ans=ans+(1<<i);
    print(ans)
    """every element occurs three times, except one element, which occurs only once. Find the element that occurs only once."""
