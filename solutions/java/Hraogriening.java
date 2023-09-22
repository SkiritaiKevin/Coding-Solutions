// https://open.kattis.com/problems/hradgreining
// Easy (1.3)

// this code relies on java's indexOf() method

import java.util.Scanner; 

public class Hraogriening{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String keyword = "COV"; 

        String sentence = scnr.nextLine();
        if(sentence.toUpperCase().indexOf(keyword.toUpperCase()) != -1){
            System.out.println("Veikur!"); 
        } 
        else{
            System.out.println("Ekki veikur!"); 
        }
        scnr.close(); 

    }
}
