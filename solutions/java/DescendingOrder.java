/*
Write a void method selectionSortDescendTrace() that takes an integer array, and sorts the array into descending order. 
The method should use nested loops and output the array after each iteration of the outer loop, thus outputting the array N-1 times (where N is the size). 
Complete main() to read in a list of up to 10 positive integers (ending in -1) and then call the selectionSortDescendTrace() method.

If the input is:

20 10 30 40 -1
then the output is:

40 10 30 20 
40 30 10 20 
40 30 20 10 
 */

import java.util.Scanner;

public class DescendingOrder {
    // an integer array and the number of elements in the array as arguments,
    // and sorts the array into descending order.
    public static void selectionSortDescendTrace(int[] numbers, int numElements) {
        int i;
        int j;
        int indexGreatest;
        int temp;

        for (i = 0; i < numElements - 1; i++) {
            indexGreatest = i;
            for (j = i + 1; j < numElements; j++) {
                if (numbers[j] > numbers[indexGreatest]) {
                    indexGreatest = j;
                }
            }

            temp = numbers[i];
            numbers[i] = numbers[indexGreatest];
            numbers[indexGreatest] = temp;
            for (int k = 0; k < numElements; k++) {
                System.out.print(numbers[k] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);

        int input, i = 0;
        int numElements = 0;
        int[] numbers = new int[10];

        // -1 is read. Then call selectionSortDescendTrace() method.

        while (scnr.hasNextInt() && i < 10) {
            input = scnr.nextInt();
            if (input == -1) {
                break;
            } else {
                numbers[i] = input;
                i++;
                numElements++;
            }
        }
        selectionSortDescendTrace(numbers, numElements);
        scnr.close();
    }
}
