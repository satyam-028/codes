#include<stdio.h>
int main(){
    int r;
    printf("Enter a number for rows:");
    scanf("%d",&r);

    int arr[r][3];

    for (int i = 0; i <r; i++){
        for (int j = 0; j <3; j++){
            scanf("%d",&arr[i][j]); 
        }
    }                                                          // do again this question

    for (int i = 0; i <r; i++){
        for (int j = 0; j <3; j++){
             printf("%d    ",arr[i][j]); 
        }
        printf("\n");
    }
    return 0;
}