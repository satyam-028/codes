import java.util.Scanner;

public class divisibleby5and3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
           int n = sc.nextInt();

         if(n%5==0 && n%3==0){ // n%15==0 this condition is also work in this program
            System.out.println("The number is divisible by 5 and 3 :");
        }

         else{
             System.out.println("The number is not divisible by 5 and 3 ");
        }


        /* if(n%5==0 && n%3!=0){
              System.out.println("The number is divisible by 5 :");
         }
          else {
              System.out.println("the number is divisible by 5 but not 3 : ");
          } */

    }
}
