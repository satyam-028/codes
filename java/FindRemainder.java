import java.util.Scanner;
public class FindRemainder {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
        System.out.println("Enter dvividend :");
        double x = sc.nextInt();
        System.out.println("Enter a divisor :");
        double y = sc.nextInt();
        double q = x/y;
        double remainder = x - (y*q);  // % also give remainder 
        System.out.println("The remainder when "+x+" is divided by "+y+" is "+remainder);

    }
}
