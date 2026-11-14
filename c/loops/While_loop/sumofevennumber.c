#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);

    int evensum = 0;
    int LastDigit = 0;
    while (n!=0)
    {
       LastDigit = n % 10;
       if(n%2==0)
         evensum = evensum + LastDigit ;
         n = n/10; 
    }
      printf("\nsum of even digit = %d",evensum);
    
    return 0;
}