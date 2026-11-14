#include<stdio.h>
int main(){
    int r;
    printf("Enter a number for rows:");
    scanf("%d",&r);
    int c;
    printf("Enter a number for column:");
    scanf("%d",&c);
    
    printf("Enter a elements in martix : ");
    int arr[r][c];
    for (int i = 0; i <r; i++){
        for (int j = 0; j <c; j++){
            scanf("%d",&arr[i][j]); 
        }

    }

    // for (int i = 0; i <r; i++){
    //     for (int j = 0; j <c; j++){
    //         printf("%d ",arr[i][j]); 
    //     }
    //     printf("\n");
    // }

    int sum = 0;
    for (int i = 0; i <r; i++){
        for (int j = 0; j <c; j++){
           sum += arr[i][j];
        }
    }
    printf("The sum of the given matrix is %d",sum); 
    return 0;
}