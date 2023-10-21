// https://open.kattis.com/problems/spavanac
// Easy (1.4)

import java.util.Scanner; 

public class Spavanac {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int hours = scnr.nextInt();
        int minutes = scnr.nextInt();
        
        minutes -= 45;
        
        if (minutes < 0) {
            hours -= 1;
            minutes += 60; 
        }

        if (hours < 0) {
            hours = 23;
        }
        
        System.out.println(hours + " " + minutes);
        scnr.close();
    }
}
