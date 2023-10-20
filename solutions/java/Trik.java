// https://open.kattis.com/problems/trik
// Easy (1.4)

import java.util.Scanner; 

public class Trik{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int position = 1; 
        String word = scnr.next();
        
        for(int i = 0; i < word.length(); i++){
            if(word.charAt(i)=='A'){
                if(position == 1){
                    position = 2; 
                }
                else if(position == 3){
                    position = 3; 
                }
                else{
                    position = 1; 
                }
            }
            else if(word.charAt(i) == 'B'){
                if(position == 2){
                    position = 3; 
                }
                else if(position == 1){
                    position = 1; 
                }
                else{
                    position = 2;
                }
            }
            else{
                if(position == 3){
                    position = 1;
                }
                else if(position == 2){
                    position = 2; 
                }
                else{
                    position = 3;
                }
            }

        }
        System.out.println(position); 

        scnr.close();
    }
}
