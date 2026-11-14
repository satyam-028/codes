#include<stdio.h>
#include<stdbool.h>
int main(){
    int arr[7] = {1,2,6,4,5,6,7};

    int x = 6;
    bool flag = false;
    int index = 0;
    for (int i = 0; i <=6; i++){
         if(arr[i]==x){
            flag = true;
            index =  i;
            break;
        }
    }
    if(flag == false){
        printf("%d is not present in the array",x);
    }
    else
        printf("%d is present in the array and its index is %d",x,index);





    // for (int i = 0; i <=6; i++){
    //      if(arr[i]==x){
    //         printf("%d is pesrent in the array and its index is %d\n",x,i);
    //         break;
    //     }
    // }



    // for (int i = 6; i >=0; i--){
    //     if(arr[i]==x){
    //         printf("%d is pesrent in the array and its index is %d\n",x,i);
    //         break;
    //     }
    // }
     
    return 0;
}