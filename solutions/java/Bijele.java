// https://open.kattis.com/problems/bijele
// Easy (1.4)

import java.util.Scanner; 

public class Bijele {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        // one king, one queen, two rooks, two bishops, two knights, eight pawns
        int[] requiredPieces = {1, 1, 2, 2, 2, 8};
        int[] foundPieces = new int[6];
        for (int i = 0; i < 6; i++) {
            foundPieces[i] = scnr.nextInt();
        }
        int[] difference = new int[6];

        for (int i = 0; i < 6; i++) {
            difference[i] = requiredPieces[i] - foundPieces[i];
        }

        for (int i = 0; i < 6; i++) {
            System.out.print(difference[i] + " ");
        }
        
        scnr.close();
    }
}
