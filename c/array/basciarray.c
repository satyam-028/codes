#include<stdio.h>
int main (){
    int arr[5] = {2,3,4,5,6};
    arr[4] = 100; // -> {2,3,4,5,100};
    printf("%d \n", arr[4]  );

    float ar[3] = {1.2,1.3,1.4};
    printf("%f \n",ar[2]);

    char arrr[4] = {'a','x','d','r'};
    printf("%c",arrr[2]);


    for (int i = 0; i <=4; i++)
    {
        int a = i + 1;
        printf("\nEnter element number %d : ", a);
        scanf("%d",&arr[i]);

    }
    printf("%d",arr[3]);



    return 0;
}