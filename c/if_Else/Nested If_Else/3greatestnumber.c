#include<stdio.h>
int main(){
    int a,b,c;
    printf("Enter a number a 1st :");
    scanf("\n%d",&a);
    printf("Enter a number a 2nd :");
    scanf("\n%d",&b); 
    printf("Enter a number a 3rd :");
    scanf("\n%d",&c);
    
    if(a>b){
        if(a>c)
        printf("greatest number  is a :");
    else 
       printf("greatest number is c ");   
    }
    
    if (b>a){
        if(b>c)
        printf("greatest number is b");
    
    else
        printf("greatest  number is c");
    }
    
    return 0;

}