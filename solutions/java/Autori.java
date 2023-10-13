// https://open.kattis.com/problems/autori
// Easy (1.2)

import java.util.Scanner; 

public class Autori {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String fullName = scnr.next(); 
        String letter = ""; 
        String[] tokens = fullName.split("-"); 
        for(int i = 0; i < tokens.length; i++){
            letter = String.valueOf(tokens[i].charAt(0)); 
            System.out.print(letter); 
        }
        scnr.close(); 
    }
}
