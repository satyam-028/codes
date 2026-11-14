import java.util.Scanner;

public class squareornot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a lenght :");
          int lenght = sc.nextInt();
        System.out.println("Enter a breadth :");
          int breadth = sc.nextInt();
        int square =lenght * breadth;

        if(lenght==breadth){
             System.out.println("yes it is square : ");
        }

        else{
            System.out.println("not a square : ");
        }
    }
}
