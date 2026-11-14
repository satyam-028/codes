import java.util.Scanner;

public class threedigitnumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a first number : ");
         int a = sc.nextInt();
        System.out.println("Enter a second number : ");
         int b = sc.nextInt();
        System.out.println("Enter a third number : ");
        int c = sc.nextInt();

        if(a>b){
            if(a>c)
             System.out.println("greatest number is a : ");
          else 
           System.out.println("greatest number is c ");   
        }
        
        if (b>a){
            if(b>c)
            System.out.println("greatest number is b");
        
           else
            System.out.println("greatest  number is c");
        }
    }
}
