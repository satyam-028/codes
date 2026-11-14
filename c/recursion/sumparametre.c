#include<stdio.h>
void sum(int n,int s){
    if(n==0){
        printf("%d",s);
        return;
    }
    sum(n-1,s+n);
   


//    int a = 0;
//     for (int i = 1; i <=n; i++)
//     {
//         a = a +i;
//     }
//     printf("%d\n",a);
    return;
}
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);
    sum(n,0);
    
    return 0;
}


