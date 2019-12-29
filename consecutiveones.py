t=int(input())
for _ in range(t):
    n=int(input())
    b=str(bin(n))[2:]
    l=b.split("0")
    print(len(max(l)))
