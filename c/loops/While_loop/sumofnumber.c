#include<stdio.h>
int main(){
    long int n; 
    printf("Enter a number :");
    scanf("%d",&n);

    long int sum = 0;
    long int LastDigit = 0;
    while (n!=0)
    {
       LastDigit = n % 10;
       sum = sum + LastDigit ;
       n = n/10; 
    }
      printf("The sum of number is %d",sum);

    return 0;
}