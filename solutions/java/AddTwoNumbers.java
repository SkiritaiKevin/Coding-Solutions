// https://open.kattis.com/problems/addtwonumbers
// Easy (1.3)

import java.util.Scanner; 

public class AddTwoNumbers {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int a = scnr.nextInt(); 
        int b = scnr.nextInt(); 
        int result = a + b; 
        System.out.println(result); 

        scnr.close(); 
    }
}
