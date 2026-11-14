#include<stdio.h>
#include<limits.h>
int main(){
    // int arr[5] = {-1,-4,-44,-3,-66};
    // // int max = arr[0];
    // int max = INT_MIN;
    // for (int i = 0; i <=4; i++){
    //     if(max<arr[i]){
    //         max = arr[i];
    //     }
    // }
    // printf("%d ",max);


   int arr[5] = {-1,-4,-44,-3,-66};
   int min = INT_MAX;
    for (int i = 0; i <=4; i++){
        if(min>arr[i]){
            min = arr[i];
        }
    }
    printf("%d ",min);



    return 0;
}