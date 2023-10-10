package asn5;

public class Asn5 {

    public static void main(String[] args) {
        MyDLList<String> strList = new MyDLList<>(); 
        MyDLList<Integer> intList = new MyDLList<>();

        strList.append("Amphicrates");
        strList.append("Lykeius"); 
        strList.append("Ayraios"); 

        intList.append(1);
        intList.append(5);
        intList.append(10);

        strList.addAfter("Cyraios", "Lykeius"); 
        intList.addAfter(7, null); 
        intList.addAfter(400, 10); 

        strList.remove("Amphicrates"); 
        intList.remove(400); 

        System.out.println(strList.toString());
        System.out.println(intList.toString()); 

        System.out.println(strList.getSize());
        System.out.println(intList.getSize());
    }
    
}
