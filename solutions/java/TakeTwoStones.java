// https://open.kattis.com/problems/twostones
// 1.3 (Easy)

import java.util.Scanner; 

public class TakeTwoStones{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int n = scnr.nextInt(); 
        if(n % 2 == 0){
            System.out.println("Bob"); 
        }
        else{
            System.out.println("Alice"); 
        }
        scnr.close(); 
    }
}