#include<stdio.h>
int main(){
    int n;
    printf("Enter a number n :");
    scanf("%d",&n);
   
    for (int i = 1; i <=n ; i++){   // outer loop -> shows no. of lines / rows
       int a = 1;
       for(int j = 1; j <=i ;j++){  // inner loop -> no. of stars in each lines / columns
          int d = a + 64;
          char ch = (char)d;
          printf("%c ",ch);
          a++;
       }
          printf("\n");   // -> backslash n meaning is enter a next line
    }
}
   // do again this question and dry run the co