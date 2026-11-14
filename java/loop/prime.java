import java.util.Scanner;


public class prime{

public static void main(String vipul[]){
    int n;

    Scanner sc= new Scanner(System.in);
    System.out.println("Enter a number :");
    n = sc.nextInt();
    int a = 0;
     for (int i = 2; i <= n-1; i++) 
     {    
         if (n%i==0)
         { 
           a = 1;
            break; 
        }
         
       
      } 
          if(n==1)
          System.out.println("1 is neither prime or composite :");
          else if(a==0)
          System.out.println("The number is prime :");
          else 
          System.out.println("This number is composite ");

}
}