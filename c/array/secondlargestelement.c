#include<stdio.h>
#include<limits.h>
int main(){
    // int arr[9] = {1,2,3,4,5,6,7,8,9};
    // int max = arr[0];
    // for (int  i = 0; i <=8; i++){
    //     if(max<arr[i])
    //     max = arr[i];
    //     max--;
    // }
    // printf("%d",max);

    int arr[7] = {1,2,3,4,4,2,1};
    // int arr[7] = {1,2,3,4,3,2,1};
    // int arr[7] = {-11,-1,-200,-2,-4,-45,0}; 
    int max = INT_MIN;
    int smax = INT_MIN;

    for (int  i = 0; i <=6; i++){
        if(max<arr[i]){
           smax = max;
           max = arr[i];
        }
        else if(smax<arr[i] && max!=arr[i]){
           smax = arr[i];
        }  

    }  
    printf("%d",smax);

    return 0;
}