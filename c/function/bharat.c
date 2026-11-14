#include<stdio.h>
void england(){
    printf("You are in england \n"); // 8
    return; //9
}
void landan(){
    printf("You are in landan \n"); //6
    england(); // caliing england.... 7
    return; //10
}
void russia(){
    printf("You are in russia \n"); //4
    landan(); // calling landan... 5
    return; //11
}
void bharat(){
    printf("You are in bharat \n"); //2
    russia(); // calling russia.... 3  
    return; //12
}
int main(){
    bharat(); //calling bharat... 1
    return 0; //13 khatam
}