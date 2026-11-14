import java.util.Scanner;

public class cpsp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a costprice :"); //printf means value ask from same line
          int cp = sc.nextInt();
        System.out.println("Enter a sellingprice :");
          int sp = sc.nextInt();

        if(sp>cp){
            System.out.print("your profit is : ");
            System.out.println(sp-cp);
        }

        if(cp>sp){
            System.out.print("your loss is : ");
            System.out.println(cp-sp);
        }
        
         if(sp==cp){
            System.out.println("no loss no profit");
        }
    }
}
