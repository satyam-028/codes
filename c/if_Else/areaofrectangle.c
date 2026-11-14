#include<stdio.h>
int main(){
    int length;
    printf("Enter a length :");
    scanf("%d",&length);
    int breadth;
    printf("Enter a breadth :");
    scanf("\n%d",&breadth);
    
    int area = length * breadth;
    int perimeter = 2 *(length + breadth);
    if(area>perimeter){
        printf("Area is greater then perimeter");
    }
    if(area<perimeter){
        printf("Permimeter is greater then area");
    }
    if(area==perimeter){
        printf("area is equal to perimter");
    }
    return 0;
}