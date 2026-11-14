#include<stdio.h>
#include<limits.h>
int main(){
   int arr[3][3] = {23,45,56,67,12,89,89,46,65};
   int min = arr[0][0];
   int max = arr[0][0];
    for (int i = 0; i <3; i++){
       for (int j = 0; j <3; j++){
         if(min>arr[i][j])
            min = arr[i][j];
         if(arr[i][j]>max)
            max = arr[i][j];
           
        }

    }
    printf("%d \n",min);
    printf("%d ",max);
    return 0;
}



//    int arr[5] = {-1,-4,-44,-3,-66};