#include<stdio.h>
int main(){
    int n; 
    printf("Enter a number :");
    scanf("%d",&n);                                                              // 1  
                                                                                 // 0 1
    // int a;                                                                       // 1 0 1
    // for (int  i = 1; i <=n ; i++){                                               // 0 1 0 1 
    //       if(i%2!=0) a = 1;  // -> This statment for start                       // 1 0 1 0 1                             
    //       else a = 0;        // -> This statment for start                                          
    //     for (int j = 1; j <=i ; j++){
    //       printf("%d ",a);
    //       if(a==0) a = 1;   // -> This statment for switch 
    //       else a = 0;       // -> This statment for switch 
    //     }
    //     printf("\n");
    // }
    

    for (int  i = 1; i <=n ; i++){
        for (int j = 1; j <=i ; j++){
            if((i+j)%2==0) printf("1 ");
            else printf("0 ");
        }
        printf("\n");
    }

}