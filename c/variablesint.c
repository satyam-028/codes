#include<stdio.h>
int main(){
    int x = 5;
    x += 6;
    printf("%d",x);
    int y = 7;
    printf("\n%d",y);
    int z = x + y;
    printf("\n%d",z);
    float q = 2, w = 4;
    printf("\n%f\n%f",q,w);
    float c = q + w;
    printf("\n%f",c);
    double r = 4, t = 33;
    printf("\n%f\n%f",r,t);
    double n = r + t;
    printf("\n%lf",n);
     
    return 0;

}