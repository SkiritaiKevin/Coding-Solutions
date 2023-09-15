package assign3_generics;

public class GenericUtility<T extends Comparable<T>> {

    private T maximumValue; 
    
    private T[] array; 

    public GenericUtility(T[] arr){
        array = arr; 
    }

    public T findMaximum(){
        maximumValue = array[0]; 

        for(int i = 0; i < array.length; i++){
            if(array[i].compareTo(maximumValue) > 0){
                maximumValue = array[i]; 
            }
        }
        return maximumValue; 
    }

    public T getMaximumValue(){
        return maximumValue; 
    }
    
    public boolean contains(T value){
        for(int i=0; i < array.length; i++){
            if(value.equals(array[i])){
                return true; 
            }
        }
        return false; 
    }
}
