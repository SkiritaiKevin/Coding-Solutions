// https://open.kattis.com/problems/timeloop
// Easy (1.3)

import java.util.Scanner; 

public class TimeLoop {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int command = scnr.nextInt(); 

        for(int i = 1; i != command + 1; i++){
            System.out.println(i + " Abracadabra"); 
        }
        scnr.close(); 
    }
}
