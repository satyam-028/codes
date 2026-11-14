import java.util.Scanner;
public class volumeofsphereinput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number is :");
        int radius = sc.nextInt();
        double pi = 3.1415;
        double volume = 4 * pi * radius * radius * radius/3;
        System.out.println("The volume of sphere is :"+volume);
        
    }
    
}
