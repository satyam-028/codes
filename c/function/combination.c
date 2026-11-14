#include<stdio.h>
int factorial(int x){
    int fact = 1;
    for (int  i = 2; i <= x; i++){
        fact = fact*i;
    }
    return fact;
}
int main(){
    int n;
    printf("Enter n : ");
    scanf("%d",&n);
    int r;
    printf("Enter r : ");
    scanf("%d",&r);
    int nfact = factorial(n); //  n!
    int rfact = factorial(r); // r!
    int nrfact = factorial(n-r); // n-r  !
    

    // for (int  i = 1; i <= n; i++){
    //     nfact = nfact*i;
    // }
    // for (int  i = 1; i <= r; i++){   // -> In this code we using 3 loops but in functions we use only 1 loop this benfit of function
    //     rfact = rfact*i;
    // }
    // for (int  i = 1; i <= n-r; i++){
    //     nrfact = nrfact*i;
   // }


    int ncr = nfact/(rfact*nrfact);  // -> int ncr = factorial(n)/factorial(r)*factorial(n-r); we use this statment also
    printf("%d",ncr);
    return 0;
}