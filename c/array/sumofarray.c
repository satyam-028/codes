#include<stdio.h>
int main(){
    int arr[5] = {2,4,3,2,6};
    int sum = 0;
    for (int i = 0; i <=4; i++){
        sum = sum + arr[i];
    }
    printf("%d ",sum);
    return 0;
}