import java.util.Scanner;

public class rectangleperimeter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a length : ");
           int length = sc.nextInt();
        System.out.println("Enter a breadth : ");
           int breadth = sc.nextInt();
        int area = length * breadth;
        int perimeter = 2 * (length+breadth);
              
         if(area>perimeter){
             System.out.println("area of rectangle is greater : ");
         }
         if(perimeter>area){
            System.out.println("perimeter of rectangle is greater : ");
         }
         if(area==perimeter) {
            System.out.println("Area and Perimeter are equal : ");
         }
    }
}
