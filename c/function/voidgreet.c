#include<stdio.h>
void greet(){
    printf("good morning \n");
    printf("satyam \n");
    return;  // return means khatam and come out from function
}
int main(){
    greet();  // call the function
    greet();
    greet();
    greet();    
    return 0;
}