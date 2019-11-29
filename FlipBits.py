t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    mb=str(bin(m))[2:]
    nb=str(bin(n))[2:]
    c=0
    if len(mb)>len(nb):
        i=0
        while i<len(mb)-len(nb):
            if mb[i]=='1':
                c+=1
            i+=1
        j=0
        while i<len(mb):
            if mb[i]!=nb[j]:
                c+=1
            i+=1
            j+=1
    elif len(mb)<len(nb):
        i=0
        while i<len(nb)-len(mb):
            if nb[i]=='1':
                c+=1
            i+=1
        j=0
        while i<len(nb):
            if mb[j]!=nb[i]:
                c+=1
            i+=1
            j+=1
    else:
        i=0
        while i<len(nb):
            if mb[i]!=nb[i]:
                c+=1
            i+=1
    print(c)
                
                
