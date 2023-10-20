// https://open.kattis.com/problems/spritt
// Easy (1.4)

import java.util.Scanner; 

public class Spritt {   
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int classrooms = scnr.nextInt(); 
        int sanitizer = scnr.nextInt(); 
        int sum = 0; 
        for(int i = 0; i < classrooms; i++){
            sum += scnr.nextInt(); 
        }
        if(sum <= sanitizer){
            System.out.println("Jebb");
        }
        else{
            System.out.println("Neibb");
        }
        scnr.close(); 
    }
}
