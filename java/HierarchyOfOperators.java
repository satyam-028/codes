public class HierarchyOfOperators {
    public static void main(String[] args) {
        double q = 2 * 3 / 4 + 7 / 4 + 8 - 2 + 5 / 8; // in this case frist solve Brackets then move left to right in case multiple and divided the addition and substors
        System.out.println(q);
        double i = 2, j = 3, k, l;
        double a, b;
        k = i / j * j;
        System.out.println("Theb value of l is :"+k);     
        l = j / i * i;
        System.out.println("Theb value of l is :"+l);     
        a = i / j * j ;
        System.out.println("Theb value of l is :"+a);     
        b = j / i * i;
        System.out.println("Theb value of l is :"+b);     
        System.out.println(k+" "+l+" "+a+" "+b);
        
    }
}
