package Exam1;

public class SortGenericArray {

    public static <T extends Comparable<T>> void insertionSort(T[] arr){
        int i; 
        int j; 
        T temp; 

        for(i = 1; i < arr.length; i++){
            j = i; 
            while(j > 0 && arr[i].compareTo(arr[j-1]) > 0){
                temp = arr[j]; 
                arr[j] = arr[j-1]; 
                arr[j-1] = temp; 
                j--; 
            }
        }
    }
}