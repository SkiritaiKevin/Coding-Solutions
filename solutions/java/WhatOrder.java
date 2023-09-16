/*
Define a generic method called checkOrder() that checks if four items are in ascending, neither, or descending order. The method should 
return -1 if the items are in ascending order, 0 if the items are unordered, and 1 if the items are in descending order.

The program reads four items from input and outputs if the items are ordered. The items can be different types, including integers, Strings, characters, or doubles.
*/
// N/A

import java.util.Scanner;

public class WhatOrder {
    // TODO: Define a generic method called checkOrder() that
    // takes in four variables of generic type as arguments.
    // The return type of the method is integer
   public static <T extends Comparable<T>> int checkOrder(T one, T two, T three, T four){
        int oneVsTwo = one.compareTo(two); 
        int twoVsThree = two.compareTo(three); 
        int threeVsFour = three.compareTo(four); 

        if(oneVsTwo > 0 && twoVsThree > 0 && threeVsFour > 0){
            return 1; 
        }
        else if(oneVsTwo < 0 && twoVsThree < 0 && threeVsFour < 0){
            return -1; 
        }
        else{
            return 0; 
        }
   }

    // Check the order of the input: return -1 for ascending,
    // 0 for neither, 1 for descending

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);

        // Check order of four strings
        System.out.println("Order: " + checkOrder(scnr.next(), scnr.next(), scnr.next(), scnr.next()));

        // Check order of four doubles
        System.out.println(
                "Order: " + checkOrder(scnr.nextDouble(), scnr.nextDouble(), scnr.nextDouble(), scnr.nextDouble()));
    }
}
