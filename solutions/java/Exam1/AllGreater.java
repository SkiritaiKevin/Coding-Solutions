package Exam1;

public class AllGreater {
    public static boolean allGreater(int[] x, int[] y) throws ArrayIndexOutOfBoundsException{
        boolean result = true; 
        try{
            for(int i=0; i<y.length; i++){
                if(y[i] >= x[i]){ 
                    result = false; 
                }
            }
            if(x.length > y.length){
                throw new ArrayIndexOutOfBoundsException("Array y was too short to perform a comparison for every element of x"); 
            }
        }
        catch(ArrayIndexOutOfBoundsException aexcpt){
            System.out.println(aexcpt.getMessage());
        }
        return result; 
    }

    public static void main(String[] args){
        int[] x = {2, 3, 5};
        int[] y = {1, 2};
        
        allGreater(x, y); 
    }
}
