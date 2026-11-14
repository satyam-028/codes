#include<stdio.h>
int factorial(int n){
    if(n==1 || n==0) return 1;  // -> if n==0 we do not write this statement and if u give output 0 then input comes out infinite
    int recAns = n*factorial(n-1);
    return recAns;
    
}
int main(){
    int n;
    printf("Enter a nmber :");
    scanf("%d",&n);
    int fact = factorial(n);
    printf("%d",fact);
    return 0;
}