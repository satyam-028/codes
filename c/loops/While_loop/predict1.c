#include<stdio.h>
int main(){
    int j;      // -> there is no value of 'j' so j cansider a grabage value they cansider any value like 2 3 4 5. 
    // printf("%d",j);
    // scanf("%d",&j);
    while (j <= 10)
    {
        printf("\n%d",j);
        j = j + 1;
    }
    
    return 0;
}