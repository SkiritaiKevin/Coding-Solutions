// https://open.kattis.com/problems/echoechoecho
// Easy (1.3)

import java.util.Scanner; 

public class EchoEchoEcho {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String word = scnr.next(); 
        System.out.println(word + " " + word + " " + word); 
        scnr.close(); 
    }
}
