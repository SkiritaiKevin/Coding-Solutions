// https://open.kattis.com/problems/knightpacking
// Easy (1.3)

import java.util.Scanner; 

public class KnightPacking{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int board = scnr.nextInt(); 
        if(board % 2 == 0){
            System.out.println("second");   
        }
        else{
            System.out.println("first");
        }
        scnr.close(); 
    }
}