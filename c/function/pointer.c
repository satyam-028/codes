#include<stdio.h>
int main(){ 
    int a = 5;
    int* x = &a; // -> int* --> int ka address store karta hai
    *x = 7;
    printf("%d\n",a); 

    int** y = &x; // -> int** --> int* store the pointer address
    int*** z = &y; 
    int**** c = &z; 
    printf("%p\n",&a);  // -> %p is use for print address 
    printf("%p",y);

//     printf("%d\n",a);
//     printf("%d\n",*x);
//     printf("%d\n",**y);
//     printf("%d\n",***z);
//     printf("%d\n",****c);

}