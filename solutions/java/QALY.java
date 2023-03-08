// https://open.kattis.com/problems/qaly
// 1.3 (Easy)

import java.util.Scanner;

public class QALY {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        double qaly = 0.0;
        for (int i = 0; i < n; i++) {
            double q = input.nextDouble();
            double y = input.nextDouble();
            qaly += q * y;
        }
        System.out.printf("%.3f\n", qaly);
    }
}
