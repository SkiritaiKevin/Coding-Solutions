package assign3_generics;

public class Assign3_Generics {
    public static void main(String[] args) {
        Integer[] nums = {1, 223, 15, 300, 17, 546, 30}; 
        String[] names = {"Kevin", "Mag", "Hama", "Prae"}; 

        GenericUtility numHelp = new GenericUtility<>(nums); 
        GenericUtility nameHelp = new GenericUtility<>(names); 

        System.out.println(numHelp.findMaximum()); // should be 546 as per test code
        System.out.println(nameHelp.findMaximum()); // should be "Prae" as per test code

        boolean result = numHelp.contains(300); // should be true
        boolean result2 = numHelp.contains(1000); // should be false

        boolean result3 = nameHelp.contains("Kevin"); // should be true
        boolean result4 = nameHelp.contains("Void"); // should be false

        System.out.println(result + ", " + result2 + ", " + result3 + ", " + result4); 




    }
    
}
