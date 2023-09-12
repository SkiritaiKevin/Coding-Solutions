// https://open.kattis.com/problems/ovissa
// 1.3 (Easy)
import java.util.Scanner; 

public class Ovissa{
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in); 
        String unnarLevel = scnr.nextLine();
        int counter = 0;  
        for(int i=0; i<unnarLevel.length(); i++){
            if(unnarLevel.charAt(i)=='u'){
                counter++;
            }
        }
        scnr.close(); 
        if(counter > 0){
            System.out.println(counter);
        } 
    }
}