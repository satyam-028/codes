#include<stdio.h>
int main(){
    int Ram;
    printf("Enter a age of Ram :");
    scanf("\n%d",&Ram);
    int Shyam;
    printf("Enter a age of Shyam :");
    scanf("\n%d",&Shyam);
    int Ajay;
    printf("Enter a age of Ajay :");
    scanf("\n%d",&Ajay);
    
    if(Ram>Shyam && Ram>Ajay){
        printf("Ram is youngest :");
    }
    if(Shyam>Ram && Shyam>Ajay){
        printf("Shyam is youngest :");
    }
    if(Ajay>Shyam && Ajay>Ram){
        printf("Ajay is youngest :");
    }
    else{
        printf("all are same age :");
    }
    
    return 0;
}