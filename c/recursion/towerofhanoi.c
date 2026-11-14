#include<stdio.h>
void towerofhanoi(int n, char s, char h, char d){
    if(n==0) return;
    tower(n-1);

}
int main(){
    int n;
    printf("Enter a number of disk  : ");
    scanf("%d",&n);
    towerofhanoi(n);
    return 0;
}
//do again this question