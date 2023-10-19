// https://open.kattis.com/problems/sorttwonumbers
// Easy (1.3)

import java.util.Scanner; 

public class SortTwoNumbers {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int a = scnr.nextInt(); 
        int b = scnr.nextInt(); 
        int smallerNumber = 0; 
        int largerNumber = 0; 

        if(a>b){
            smallerNumber = b; 
            largerNumber = a;  
        }
        else{
            smallerNumber = a; 
            largerNumber = b; 
        }

        System.out.println(smallerNumber + " " + largerNumber); 
        scnr.close(); 
    }
}
