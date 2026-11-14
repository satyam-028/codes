#include<stdio.h>
int main(){
    int arr[4];
    printf("Enter a numbers : ");
    // int arr[7] = {1,2,3,4,5,6,7};
    for (int i = 0; i <=6; i++){
        scanf("%d ",&arr[i]);
    }
    printf("\nArray elementd : ");
    int count = 0;
    int x = 4;
    for (int i = 0; i <=3; i++){
        if(arr[i]>x) count++;
        if(arr[i]<x) printf("dshtkyf");
    }

    for (int i = 0; i <=3; i++){
       printf("%d ",arr[i]);
    } 
}