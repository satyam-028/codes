#include<stdio.h>
int main(){
    double x1,y1,x2,y2,x3,y3;
    printf("Enter a number 1st :");
    scanf("%lf",&x1);
    printf("Enter a number 2nd :");
    scanf("%lf",&y1);
    printf("Enter a number 3rd :");
    scanf("%lf",&x2);
    printf("Enter a number 4th :");
    scanf("%lf",&y2);
    printf("Enter a number 5th :");
    scanf("%lf",&x3);
    printf("Enter a number 6th :");
    scanf("%lf",&y3);
    
    double m1 = (y2 - y1) / (x2 - x1);
    double m2 = (y3 - y2) / (x3 - x2);
    
    if(m1=m2){
        printf("lies on the same line :");
    }
    else{
        printf("they not lie on the same line :");
    }

    return 0;
}