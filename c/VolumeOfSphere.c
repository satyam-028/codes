#include<stdio.h>

int main(){
    float r;
    printf("enter a number :");
    scanf("%f",&r);
    float v = 4 * 3.1415 *  r * r * r / 3;
    printf("the volume is :%f",v); 

    return 0;

}
