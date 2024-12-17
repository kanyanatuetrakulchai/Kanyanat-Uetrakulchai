public class CovidReporter {
    public static void main(String[] args) {
        CovidProfile s1 = new CovidProfile();
        s1.setDate("2021-01-29");
        s1.setLocation("France");
        s1.setACCCases(985);
        s1.setCuredCases(5600);
        s1.setDeathCases(6000);
        s1.printPatientInfo();
        // System.out.println("Currently, there are " + Student.all_students + "
        // students.");

        // Student s2 = new Student("Suppawong", "Male", 24, 4.00);
        // s2.printStudentInfo();
        // System.out.println("Currently, There are " + Student.all_students + "
        // students.");
    }
}
