// https://open.kattis.com/problems/cold
// Easy (1.3)

import java.util.Scanner; 

public class ColdputerScience {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int numTemps = scnr.nextInt(); 
        int[] temps = new int[numTemps];  
        
        for(int i = 0; i < numTemps; i++){
            temps[i] = scnr.nextInt(); 
        }

        int negCounter = 0; 
        for(int i = 0; i < numTemps; i++){
            if(temps[i] < 0){
                negCounter++; 
            }
        }
        System.out.println(negCounter); 
        scnr.close(); 
    }
}
