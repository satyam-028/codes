import java.util.Scanner;

public class Digit3number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number :");
         int n = sc.nextInt();
        
         if(n>99 && n<1000){ // in two digit number condidtion is n>10 && n<100 
             System.out.println("The number is three digit number :");
         }

         else{
             System.out.println("The number is not three digit number :");
         }
    }
}
