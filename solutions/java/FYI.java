// https://open.kattis.com/problems/fyi
// Easy (1.3)

import java.util.Scanner; 

public class FYI {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String dir = scnr.next();
        int prefix = Integer.parseInt(dir.substring(0,3)); 

        if(prefix == 555){
            System.out.println(1);
        }
        else{
            System.out.println(0); 
        }

        scnr.close();
    }    
}
