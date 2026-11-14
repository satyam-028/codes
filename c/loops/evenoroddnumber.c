#include<stdio.h>
int main(){
    printf("This numbers is even :");  
    
    for (int i = 1; i <= 100; i++)
    {
        if(i%2==0)
            printf(" %d ",i);

    }
    
    printf("\nThis numbers is odd :");  
    for (int i = 1; i <= 100; i++){

        if(i%2!=0)
           printf(" %d ",i);
    }
    
    return 0;
}