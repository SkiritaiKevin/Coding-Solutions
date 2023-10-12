package GroceryShoppingList; 

import java.util.Scanner;
import java.util.LinkedList;

public class ShoppingList {
   public static void main (String[] args) {
      Scanner scnr = new Scanner(System.in);

      // TODO: Declare a LinkedList called shoppingList of type ListItem
      LinkedList<ListItem> itemlis = new LinkedList<ListItem>(); 

      // TODO: Scan inputs (items) and add them to the shoppingList LinkedList
      //       Read inputs until a -1 is input

      String item; 
      while(true){
        item = scnr.nextLine(); 
        if(item.equals("-1")){
            break; 
        }
        itemlis.add(new ListItem(item)); 
      }
      
      // TODO: Print the shoppingList LinkedList using the printNodeData() method
      for(ListItem lisItem : itemlis){
        lisItem.printNodeData(); 
      }
    
      scnr.close(); 
   }
}