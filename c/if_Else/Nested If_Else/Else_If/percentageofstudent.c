#include<stdio.h>
int main(){
    int n;
    printf("Enter a percentage :");
    scanf("\n%d",&n);
    
    if (n>80)
    {
       printf("A grade excllent :");
    }
    else if(n>60){
        printf("B grade and you can do better :");
    }
    else if(n>40){
        printf("c grade and average : ");
    }
    else{
        printf("D garde and below average :");
    }
    return 0;
    
}