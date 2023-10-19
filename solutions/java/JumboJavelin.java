// https://open.kattis.com/problems/jumbojavelin
// Easy (1.3)

import java.util.Scanner; 

public class JumboJavelin {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int numRods = scnr.nextInt();
        int sum = 0;
        for(int i = 0; i < numRods; i++){
            sum += scnr.nextInt(); 
        }
        int result = sum - (numRods - 1); 
        System.out.println(result); 
        scnr.close(); 
    }    
}
