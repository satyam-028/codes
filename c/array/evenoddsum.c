#include<stdio.h>
int main(){
    int arr[5] = {1,2,3,4,5};
    int SumEven = 0; // -> 1 + 3 + 5 = 9
    int SumOdd = 0;  // -> 2 + 4 = 6
    for (int i = 0; i <=4; i++)
    {
       if(i%2==0)
        SumEven += arr[i];
                                                
    else{
      SumOdd += arr[i];
    }

    }
    int res =  SumEven - SumOdd; // -> 9 - 6 = 3
    printf("%d ",res);
    return 0;
}