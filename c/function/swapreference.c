#include<stdio.h>
void swap(int* x, int* y){
    int temp;
    temp = *x;  // temp = a
    *x = *y;    // a = 9
    *y = temp;  // *y = 4 -> b = 4;
    return;
}
int main(){
    int a = 4;
    int b = 9;
    swap(&a,&b);  // -> pass by reference means address pass krna 
    
    printf("The Value of a is %d\n",a);
    printf("The Value of b is %d",b);
}

