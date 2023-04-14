// https://open.kattis.com/problems/jackolanternjuxtaposition
// 1.2 (Easy)

import java.util.Scanner; 

public class Jack {
    public static void main(String[]args){
        Scanner input = new Scanner(System.in); 
        
        int n = input.nextInt(); 
        int t = input.nextInt();   
        int m = input.nextInt(); 
        
        int numDesigns = n * t * m; 
        
        System.out.println(numDesigns); 
    }
}
