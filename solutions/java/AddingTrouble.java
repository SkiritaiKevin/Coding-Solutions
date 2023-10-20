// https://open.kattis.com/problems/addingtrouble
// Easy (1.3)

import java.util.Scanner; 

public class AddingTrouble {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in);
        int a = scnr.nextInt(); 
        int b = scnr.nextInt(); 
        int c = scnr.nextInt(); 

        if(a+b==c){
            System.out.println("correct!");
        }
        else{
            System.out.println("wrong!");
        }

        scnr.close();
    }
}
