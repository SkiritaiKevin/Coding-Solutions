// https://open.kattis.com/problems/vidsnuningur
// Easy (1.3)

import java.util.Scanner;

public class Viosnuningur{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String words = scnr.next(); 
        String wordsReversed = ""; 

        for(int i=0; i < words.length(); i++){
            wordsReversed = words.charAt(i) + wordsReversed; 
        }

        System.out.println(wordsReversed); 
        scnr.close(); 
    }
}