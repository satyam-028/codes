#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);

    int a = 0;
     for (int i = 2; i <= n-1; i++) // -> n-1 means 24-1 24 is n so this loop work only 23 times
     {    // int i = 2 3 5 7 23 29
         if (n%i==0)
         { 
            a = 1;
         //   printf("This number is composite \n");
           
            break;  // -> if we not use break statment "This number is composite " print many times
         }
         
         // else{
         //    printf("the number is prime number\n");
         //    break;
         // }
      } 
          if(n==1)
             printf("1 is neither prime or composite :");
          else if(a==0)
             printf("The number is prime :");
          else 
             printf("This number is composite ");

}
// }