#include<stdio.h>
int main(){
    int marks[10] = {96,65,90,45,34,15,54,23,33,99};
    for (int i = 0; i <=9; i++) if(marks[i]<35) printf("%d ",i);
    
  
    
    // for (int i = 0; i <=4; i++){
    //   printf("Enter element number %d\n",i+1);
    //   scanf("%d ",&marks[i]);
    //   if(marks[i]<35) printf("%d ",i);
    // }
  
    return 0;
}