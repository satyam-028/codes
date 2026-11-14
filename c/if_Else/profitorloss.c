#include<stdio.h>
int main(){
    int cp;
    printf("enter cost price :");
    scanf("%d",&cp);
    int sp;
    printf("enter selling price :");
    scanf("%d",&sp);
    
    if(sp>cp){
        printf("profit");
    }
    if (cp>sp){
        printf("loss");
    }
     if (sp==cp){
         printf("no profit or no loss");
    }
    return 0;
}