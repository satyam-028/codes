import java.util.Scanner;

public class origin {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       System.out.println("Enter a first number : ");
        int x = sc.nextInt();
       System.out.println("Enter a second number : ");
        int y = sc.nextInt();

          if(x==0 && y==0){
             System.out.println("The points is origin : ");
          }

          else if(x==0){
              System.out.println("lie on y-axis : ");
          }

          else{
             System.out.println("lie on x-axis : ");
          }
    }
}
