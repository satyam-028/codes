#include<stdio.h>
int main(){
    double x,y;
    printf("Enter a coordinate 1st :");
    scanf("%lf",&x);
    printf("Enter a coordinate 2nd :");
    scanf("%lf",&y);
    
    if (x==0 && y==0)
    {
        printf("the points is origin :");
    }
    else if(x==0){
        printf("lies on y-axis :");
    }
    else{
      printf("lies on x-axis :");
    }
    return 0;
}