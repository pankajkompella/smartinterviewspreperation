#include<stdio.h>
#include<math.h>
void main()
{
 int cnt = 0; 
 int n;
 scanf("%d",&n);
    for (int i = 1; i <= sqrt(n); i++) { 
        if (n % i == 0) { 
            // If divisors are equal, 
            // count only one 
            if (n / i == i) 
                cnt++; 
  
            else // Otherwise count both 
                cnt = cnt + 2; 
        } 
    } 

printf("%d",cnt);
}
