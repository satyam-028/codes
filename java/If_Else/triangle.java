import java.util.Scanner;

public class triangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a first number : ");
          int a = sc.nextInt();
        System.out.println("Enter a second number : ");
          int b = sc.nextInt();
        System.out.println("Enter a third number : ");
          int c = sc.nextInt();
          
           if(a+b>c && b+c>a && a+c>b){
                System.out.println("Valid triangle :");
           }

           else{
              System.out.println("not valid triangle :");
           }
    }
}
