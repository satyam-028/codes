#include<stdio.h>
void increasing(int a,int n){
    if(a>n)  return;
    printf("%d\n",a);
    increasing(a+1,n);


 
    // int a;
    // for (int i = 1; i <=n; i++)
    // {
    //     a = a +1;
    //     printf("%d\n",i);
        
    // }
    return;
}
int main(){
    int n;
    printf("Enter a number :");
    scanf("%d",&n);
    int a;
    increasing(1,n);

    return 0;
}

