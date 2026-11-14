#include<stdio.h>
int main(){
    // int n;
    // printf("Enter a number :");
    // scanf("%d",&n);
     
       //AP -> 1,3,5,7,9.......so on
    // for (int i = 1; i <= n; i=i+2) //for(int i = 1; i <= 2*n-1; i++) this statment is using maths 
    // {
    //     n = n + 1;
    //     printf(" %d ",i);
         
    // }


       //AP -> 4,7,10,13,16.......so on
    // for (int i = 1; i <= n; i++)
    // {
    //     n = n + 3;
    //     printf(" %d ",i);
    // }

    
    //   do again this question bhai

      

      //Decreasing AP -> 100,97,94......so on, print all positive number 
    int a = 100;
    
    for (int i = 1;a > 0; i++)
    {
          printf(" %d ",a);
          a = a - 3;   
    }
    

      

}