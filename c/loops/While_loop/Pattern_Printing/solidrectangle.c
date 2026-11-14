#include<stdio.h>
int main(){
    int n,m;
    printf("Enter a number n :\n");
    printf("Enter a number m :\n");
    scanf("%d%d",&n,&m);
    for (int i = 1; i <=n ; i++){   // outer loop -> shows no. of lines / rows
       for(int i = 1; i <=m ;i++){  // inner loop -> no. of stars in each line / columns
          printf("*");
       }
          printf("\n");   // -> backslash n meaning is enter a next line
    }
}