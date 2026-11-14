#include<stdio.h>
int main(){
    int n;
    printf("Enter a number :");
    scanf("\n%d",&n);
    
    if(n%2==0){
        printf("The number is even :");  // if(n%2!==0) in next line we write this equation its also work same
    }
    else{
        printf("the  number is odd :");
    }
    return 0;
}