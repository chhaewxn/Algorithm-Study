#include <stdio.h>
#include <math.h>
 
void kanto(int n)
{
    int num = pow(3, n - 1);
    if (n == 0)
    {
        printf("-");
        return;
    }
    kanto(n - 1);
    for (int i = 0; i < num; i++)
    {
        printf(" ");
    }
    kanto(n - 1);
}
 
 
int main()
{
    int n;
    while (scanf("%d", &n)!=EOF)
    {
        kanto(n);
        printf("\n");
    }
    return 0;
}
 