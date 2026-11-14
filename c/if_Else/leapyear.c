#include<stdio.h>
int main(){
    int n;
    printf("Enter a year :");
    scanf("\n%d",&n);
    
    if(n%4==0){
        printf("This is leap year :");
    }
    else{
        printf("This not leap year");
    }
    return 0;
}