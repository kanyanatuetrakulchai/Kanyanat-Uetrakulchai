import java.util.Scanner;
public class BMICalculator {
	public static void main(String[] args) {
		//Name: Kanyanat Uetrakulchai
		//ID: 6687007
		//Section: 2
		Scanner scanner = new Scanner(System.in);
		
		double weight = scanner.nextDouble();
		double height = scanner.nextDouble();
		double BMI = weight/(height * height);
		System.out.println("Your BMI is "+ String.format("%.2f", BMI));
		if (BMI < 18.5) {
			System.out.print("Underweight");
		} else if (BMI >= 18.5 && BMI < 24.9) {
			System.out.print("Normal weight");
		} else if (BMI >= 29.9 && BMI < 29.9) {
			System.out.print("Overweight");
		} else {
			System.out.print("Obesity");
		}
		scanner.close();
 }
}