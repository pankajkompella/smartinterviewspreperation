t=int(input())
for _ in range(t):
    n=int(input())
    i=5
    p=0
    while n//i!=0:
        p+=n//i
        i*=5
    print(p)
