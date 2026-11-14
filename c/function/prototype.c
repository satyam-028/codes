#include<stdio.h>

int main(){
    void fun();  // -> this statment called function prototype
    fun();
    return 0;
}
void fun(){
    printf("hello");
    return;
}
// int main(){
//     fun();
//     return 0;
// }
  


 // -> function prototype is kind of useless