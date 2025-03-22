import java.util.Scanner;

public class Bhaskara {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user to enter coefficients a, b, and c
        System.out.println("Enter coefficients a, b, and c:");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        // Calculate the discriminant
        double discriminant = b * b - 4 * a * c;

        // Check if the discriminant is non-negative
        if (discriminant >= 0) {
            // Calculate the two roots
            double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);

            // Print the roots
            System.out.println("Root 1: " + root1);
            System.out.println("Root 2: " + root2);
        } else {
            // If the discriminant is negative, there are no real roots
            System.out.println("The equation has no real roots.");
        }

        scanner.close();
    }
}