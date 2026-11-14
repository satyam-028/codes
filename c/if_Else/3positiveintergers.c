#include<stdio.h>
int main(){
    int a,b,c;
    printf("Enter a number :");
    scanf("\n%d%d%d",&a,&b,&c);
    
    if(a>b && a>c){
        printf("The value of a is greatest :");
    }
    if(b>c && b>a){
        printf("The value of b is greatest :");
    }
    if(c>a && c>b){
        printf("The vlaue of c is greatest :");
    }
    if(a=b=c){
        printf("The vlaue of a b and c is equal :");
    }
    return 0;
}