#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);

      //GP -> 1,2,4,8,16,32......so on 
    // int a = 1;
    // for (int i = 1; i <= n; i++)
    // {
    //     printf(" %d ", a);
    //     a = a * 2;
    // }
      

      //GP -> 3,12,48......so on
    // int a = 3;
    // for (int i = 1; i <= n; i++)
    // {
    //     printf(" %d ", a);
    //     a = a * 4;
    // }


      //Decreasing GP -> 100,50,25......so on and print all posotive number 
    float a;
    for (int i = 1; i <= n; i++)
    {
        printf(" %d ",a);    // do again this question bhai
        a = a * 1/2;
    }
      
    
}