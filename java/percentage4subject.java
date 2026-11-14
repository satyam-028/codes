public class percentage4subject {
    public static void main(String[] args) {
        int maths = 53;   //variable name not start from number and espasical keys not allow and  keys wards not allow
        int english = 11;
        int hindi = 22;
        int sanskarit = 55;
        int sum =maths+english+hindi+sanskarit; 
        int totalPossibleMarks = 240;//60*no of subjects
        double percentages = sum*100/totalPossibleMarks;
        System.out.println(percentages);
    }
}
