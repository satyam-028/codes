// package oops;

public class studentclass {
    public static class student{
        String name;
        int rno;
        double percent;
    } 
    public static void main(String[] args) {
        student s1 = new student();
        s1.name = "satyam";
        s1.rno = 63;
        s1.percent = 76;
        System.out.println(s1.name);
        System.out.println(s1.rno + 2);
        System.out.println(s1.percent + 2);
        // System.out.println(s1.age);
    }
}