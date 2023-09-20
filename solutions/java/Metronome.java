// https://open.kattis.com/problems/metronome
// Easy (1.2)

import java.util.Scanner;

public class Metronome {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int n = scnr.nextInt(); 
        double numRevs = n / 4.00;
        
        System.out.println(numRevs); 

        scnr.close(); 
    }
}
