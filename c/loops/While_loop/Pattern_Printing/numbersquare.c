#include<stdio.h>
int main(){
    int n;
    printf("Enter a number n :");
    scanf("%d",&n);
    for (int i = 1; i <=n ; i++){   // outer loop -> shows no. of lines / rows
       for(int i = 1; i <=n ;i++){  // inner loop -> no. of stars in each lines / columns
          printf("%d ",i);
       }
          printf("\n");   // -> backslash n meaning is enter a next line
    }
}