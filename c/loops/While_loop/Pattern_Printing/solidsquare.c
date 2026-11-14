#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);
    for (int i = 1; i <=n ; i++){   // outer loop -> shows no. of lines / rows
       for(int i = 1; i <=n ;i++){  // inner loop -> no. of stars in each line / columns
          printf("*  ");
       }
          printf("\n");   // -> backslash n meaning is enter a next line
    }
}  