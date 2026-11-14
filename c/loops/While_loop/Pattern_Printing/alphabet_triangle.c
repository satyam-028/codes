#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);


    for (int i = 1; i <=n ; i++){
        for (int j = 1; i <=n-i ; i++){
           printf(" ");
        }
        int a = 1;
        for (int k = 1; k <=a ; k++)
        {
          int d = a + 64;
          char ch = (char)d;
          printf("%c ",ch);
          a++;
        }
        printf("\n");
    }
    
} 
     // do again this question