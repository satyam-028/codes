import java.util.Scanner;

public class gradeelse_if {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter percantages : ");
          double n = sc.nextInt(); // n -> percantage

          if(n>90){
             System.out.println("Excellent :");
          }

          else if(n>80){
             System.out.println("Very good :");
          }

          else if(n>70){
             System.out.println("good you :");
          }

          else if(n>60){
             System.out.println("can do better :");
          }

          else if(n>50){
             System.out.println("Average :");
          }

          else if(n>40){
             System.out.println("below Average :");
          }

          else{
             System.out.println("Fail better luck next time :");
          }
    }
}
