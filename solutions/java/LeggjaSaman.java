// https://open.kattis.com/problems/leggjasaman
// 1.3 (Easy)

import java.util.Scanner; 

public class LeggjaSaman{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        int n = scnr.nextInt();
        int m = scnr.nextInt(); 
        int totalCars = n + m; 
        System.out.println(totalCars); 
        scnr.close(); 
    }
}
