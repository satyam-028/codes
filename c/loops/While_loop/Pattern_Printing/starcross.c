#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);

    for (int i = 1; i <=n ; i++){     // outer loop -> shows no. of lines / rows
      for (int j = 1; j <=n ; j++){   // inner loop -> no. of stars in each line / columns
         if(i==j || i+j==n+1)
           printf("*");
         else
          printf(" ");
    }
    printf("\n");
    
    }




   
  //  for (int i = 1; i <=n ; i++){                        //  ********
  //      for (int j = 1; j <=n ; j++){                    //     *
  //        if(i==1 || j==3) printf("*");                  //     *
  //        else printf(" ");                              //     *
  //      }                                                //     *
  //      printf("\n ");                                   //     *
  //  } 
  
    
} 
   // -> do again this question