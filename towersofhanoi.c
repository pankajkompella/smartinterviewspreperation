#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    void towers(int n,char src,char dest,char aux)
    {
        if(n==1)
        {
            printf("Move %d from %c to %c\n",n,src,dest);
            return;
        }
        towers(n-1,src,aux,dest);
        printf("Move %d from %c to %c\n",n,src,dest);
        towers(n-1,aux,dest,src);
    }  
    int t,n;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d",&n);
        printf("%d\n",(1<<n)-1);
        towers(n,'A','C','B');
    }
    return 0;
}
