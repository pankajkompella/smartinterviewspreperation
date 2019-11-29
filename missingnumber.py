t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    t=(n+1)*(n+2)//2
    s=sum(l)
    print(t-s)
