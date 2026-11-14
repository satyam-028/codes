#include<stdio.h>
int main(){
    float principle,rate,time,si;
    printf("\nEnter princciple :");
    printf("\nEnter rate :");
    printf("\nEnter a time :");
    scanf("%f%f%f",&principle,&rate,&time);
    si = (principle*rate*time)/100;
    printf("your ssimple interset is : %f",si);
    return 0;
}