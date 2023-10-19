// https://open.kattis.com/problems/digitswap
// Easy (1.3)

import java.util.Scanner; 

public class DigitSwap {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String a = scnr.next(); 
        StringBuilder num = new StringBuilder(a); //https://stackoverflow.com/questions/28479226/how-to-deal-with-integers-and-flip-them
        num.reverse(); 
        int i = Integer.parseInt(num.toString());
        System.out.println(i); 
        scnr.close(); 
    }
}
