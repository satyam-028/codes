#include<stdio.h>
int main(){
    long int n;
    printf("Enter a number :");
    scanf("%d",&n);
    
    long int count = 0;
    while (n>0)
    {
        n = n/10;
        count++;
    }
      printf("The no of digit are %d",count);
    
    return 0;
}