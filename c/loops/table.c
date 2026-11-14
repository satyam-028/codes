#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf(" %d ",&n);
     
    for (int i = 1; i <= 10; i++)
    {
        printf(" %d*%d = %d ",n,i,(n*i));
    }
     

    //  for (int i = 19; i <= 190; i=i+19)
    //  {
    //      printf(" %d ",i);
    //  }
     
}