#include<stdio.h>
int add(int X, int Y){
    return X+Y;
}
int main(){
    int a;
    printf("Enter a number :");
    scanf("%d",&a);
    int b;
    printf("Enter a number :");
    scanf("%d",&b);
    int sum = add(a,b);
    printf("%d",sum);
    return 0;
}