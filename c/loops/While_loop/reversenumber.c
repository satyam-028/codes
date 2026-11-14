#include<stdio.h>
int main(){
    int n;
    printf("Enter any number :");
    scanf("%d",&n);

    int r = 0;
    int sum = 0;
    while (n!=0) // -> n>0
    {
       r = r + (n%10);   /* -> if you replace this statment r = r + (n%10); and  r = r * 10; you have not to be use this statment */
       r = r * 10;
       n = n/10;
    //    sum = r + n;
    }
    r = r/10;

      printf("The revers number is %d\n",r);
    //   printf("The sum of number is %d\n",+sum);
    return 0;
}