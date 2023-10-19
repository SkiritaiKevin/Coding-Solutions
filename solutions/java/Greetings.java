// https://open.kattis.com/problems/greetings2
// Easy (1.3)

import java.util.Scanner;

public class Greetings{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the input string
        String inputString = scanner.nextLine();

        // Check if the input starts with "he...ey" pattern
        if (inputString.startsWith("he")) {
            // Double the number of 'e's in the greeting
            int inputLength = inputString.length();
            int responseLength = 2 * (inputLength - 2); // Double the number of 'e's
            StringBuilder response = new StringBuilder("h");
            for (int i = 0; i < responseLength; i++) {
                response.append("e");
            }
            response.append("y");

            System.out.println(response.toString());
        } else {
            // If the input does not match the pattern, print an error message
            System.out.println("Invalid input");
        }

        scanner.close();
    }
}
