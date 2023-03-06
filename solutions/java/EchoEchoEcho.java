// https://open.kattis.com/problems/oddecho
// 1.3 (Easy)

import java.util.Scanner;

public class EchoEchoEcho {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = sc.next();
        }
        for (int i = 0; i < n; i += 2) {
            System.out.println(words[i]);
        }
        sc.close();
    }
}
