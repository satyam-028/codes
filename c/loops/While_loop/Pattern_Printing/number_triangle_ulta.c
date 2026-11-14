#include<stdio.h>
int main(){
    int n;
    printf("Enter a number n :");
    scanf("%d",&n);
    for (int i = 1; i <=n ; i++){   // outer loop -> shows no. of lines / rows
       for(int j = 1; j <=n+1-i ;j++){  // inner loop -> no. of stars in each line / columns
           printf("%d ",j);
       }
          printf("\n");   // -> backslash n meaning is enter a next line
    }
}

