// https://open.kattis.com/problems/findingana
// Easy (1.3)

import java.util.Scanner; 

public class FindingAnA {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String word = scnr.next(); 
        String suffix = "";
        for(int i = 0; i < word.length(); i++){
            if(word.charAt(i) == 'a'){
                suffix = word.substring(i, word.length()); 
                break; 
            }
        }
        System.out.println(suffix); 
        scnr.close(); 
    }
}
