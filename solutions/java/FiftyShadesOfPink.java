// https://open.kattis.com/problems/fiftyshades
// Easy (1.5)

import java.util.Scanner; 

public class FiftyShadesOfPink {
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in);
        String pink = "pink";
        String rose = "rose"; 
        String word = "";
        int counter = 0; 
        int lines = scnr.nextInt(); 

        for(int i = 0; i < lines; i++){
            word = scnr.next(); 
            if(word.toLowerCase().contains(pink) == true || word.toLowerCase().contains(rose) == true){
                counter++; 
            }
        }
        if(counter == 0){
            System.out.println("I must watch Star Wars with my daughter");
        }
        else{
            System.out.println(counter);
        }
        scnr.close();
    }
}
