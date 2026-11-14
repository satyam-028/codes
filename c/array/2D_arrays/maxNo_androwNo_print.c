#include<stdio.h>
#include<limits.h>

int main(){
    int arr[3][4] = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
    int maxSum = INT_MIN;
    int index = -1;
    for (int i = 0; i <=3; i++){
        int sum = 0;
        for (int j = 0; j <=4; j++){
            sum += arr[i][j];
        }
        if (sum > maxSum){
           maxSum = sum;
           index = i;
        }
       
    }
    printf("%d\n",maxSum);
    printf("%d",index);
    return 0;
}

// do again question

