#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("\n%d",&n);
    
    if(n%5==0){
        printf("The number is divisible by 5 :");  
    }
    else{
        printf("the  number not divisible by 5 :");
    }
    return 0;
}