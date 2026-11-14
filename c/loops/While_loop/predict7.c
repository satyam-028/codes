#include<stdio.h>
int main(){
    int i;
    while (i==10)  // -. infinite loop because condition given is i=10 
    {
        printf("\n%d",i);
        i = i + 1;
    }
    
    return 0;
}