#include<stdio.h>
int main(){
    int arr[4][4] = {23,45,56,23,67,12,89,43,89,46,65,86,65,98,99,23};
    int result[4][4];
    for (int i = 0; i <2; i++){
        for (int j = 1; j <3; j++){
            result[i][j] = arr[i][j] + arr[i][j];
            printf("%d  \n",result);
        }                                                                         
        printf("\n");
    }
    
    return 0;
}

// do again this question 


// 23 45 56 23 
// 67 12 89 43 
// 89 46 65 86 
// 65 98 99 23 