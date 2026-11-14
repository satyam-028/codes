import java.util.Scanner;

public class notdivisibleny15 {
    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     System.out.println("Enter a number : ");
       int n = sc.nextInt();

        if(n%5==0 || n%3==0){
            if(n%15!=0){
                System.out.println("The number is divisible by 5 and 3 but not 15 : ");
            }

             else{
                System.out.println("not matching requrid condition : ");
             }
        }
             else{
                 System.out.println("not matching requrid condition : ");
             }
    }
}
