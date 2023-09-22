package Exam1;

import java.util.Scanner; 

public class MealTip {

    // has errors cause we assume this is part of main program for test

    Scanner scnr = new Scanner(System.in); 
    double meal;
    double tip; 
    boolean needInput = true; 
    while(needInput){
        try{
            meal = scnr.nextDouble(); 
            tip = scnr.nextDouble(); 
            if(tip > meal){
                System.out.println("Do you want to give such a large tip? Enter 1 for yes and 2 for no:");
                int userAnswer = scnr.nextInt(); 
                if(userAnswer == 1){
                    needInput = false; 
                }
                else{
                    scnr.nextLine(); 
                }
            }
            else{
                needInput = false; // if meal greater than tip just end
            }
        }
        catch(InputMismatchException iexcpt){
            System.out.println("Please enter numeric values (EX: '12.50') "); 
            scnr.nextLine(); 
        }
    }
}
}
