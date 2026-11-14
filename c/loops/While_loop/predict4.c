#include<stdio.h>
int main(){
    int x = 4,y,z;
    y = --x;  // y = x = x - 1
    z = x--;  
    printf("\n%d%d%d",x,y,z);

    return 0;
}