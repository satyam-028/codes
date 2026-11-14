
import java.util.Scanner;
public class squareofnumberinput {

        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number :");
        int x = sc.nextInt();
        double n = x * x;
        System.out.println("The number of square is :"+n);
        sc.close();
    }
    
}
