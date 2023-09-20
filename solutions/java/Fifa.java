// https://open.kattis.com/problems/fifa
// Easy (1.3)

import java.util.Scanner; 

public class Fifa{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        final int initialYear = 2022; 
        try{
            int n = scnr.nextInt(); 

            if(n < 0 || n > 1000){
                throw new Exception("Input for n is faulty"); 
            }

            int k = scnr.nextInt(); 

            int addToYears = n/k; 
            int result = initialYear + addToYears; 
            System.out.println(result); 

            
        }
        catch(Exception e){
            System.out.println(e.getMessage()); 
        }

    }
}
