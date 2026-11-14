#include<stdio.h>
int main(){
   int arr[3][3] = {23,45,56,67,12,89,89,46,65};
   
    for (int i = 0; i <3; i++){
       for (int j = 0; j <3; j++){
         printf("arr[%d][%d] = %d\n",i,j,arr[i][j]); 
      }
    }
    
}