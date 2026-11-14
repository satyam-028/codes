#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);
    
    // => 1 2 3 4 5 6  7  8  9 10 11 this is a place of numbers
    // -> 1 1 2 3 5 8 13 21 34 55 89......and so on this is all fucking fibonacci number 
    // -> In this case we need to creat 3 variables because we store a value. value is 1+1 'a+b'
    int a = 1;
    int b = 1;
    int sum = 1; // -> sum = 1 
    for (int i = 1; i <= n-2; i++)  // -> (n-2) If we not use this condition and we use (n) so place of number is change
    {
        sum = a + b;
        a = b;
        b = sum;
        printf("The %d fibonacci is :%d\n",i,sum);
    }
    // printf("The fibonacci number is %d :",sum);

}