class student {
    int rollno;
    String name;
    void printDetails()
    {
        System.out.println("Roll No:"+rollno);
        System.out.println("Name:"+name);
    }
}
public class studentdetails{
    public static void main(String[] args) {
        student s1,s2;
        s1 = new student();
        s2 = new student();

        s1.rollno = 34;
        s1.name = "satyam";
        s2.rollno = 44;
        s2.name = "shivam";
        s1.printDetails();
        s2.printDetails();
        
    }
}