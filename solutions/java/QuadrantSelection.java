// https://open.kattis.com/problems/quadrant
// Easy (1.3)

import java.util.Scanner; 

public class QuadrantSelection {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int x = scnr.nextInt();
        int y = scnr.nextInt(); 

        if(x < 0){
            if(y < 0){
                System.out.println(3); 
            }
            else{
                System.out.println(2);
            }
        }
        else{
            if(y < 0){
                System.out.println(4);
            }
            else{
                System.out.println(1);
            }
        }

        scnr.close();
    }
}
