import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.text.DecimalFormat;

public class Solution {  
  
    static DecimalFormat format = new DecimalFormat("0.0");  

    private static void addNumber(int n,
                                  PriorityQueue<Integer> lowerHalf,
                                  PriorityQueue<Integer> upperHalf){
        if(lowerHalf.size() == 0 || n < lowerHalf.peek() ){
            lowerHalf.add(n);
        }                           
        else{
            upperHalf.add(n);
        }
    }

    private static void balanceHeaps(PriorityQueue<Integer> lowerHalf,
                                     PriorityQueue<Integer> upperHalf) {
       if(lowerHalf.size() - upperHalf.size() >= 2){
            upperHalf.add(lowerHalf.poll());
       }
       else if(upperHalf.size() - lowerHalf.size() >= 2) {
           lowerHalf.add(upperHalf.poll());
       }  
    }

    private static double calculateMedian(PriorityQueue<Integer> lowerHalf,
                                          PriorityQueue<Integer> upperHalf) {
        if(lowerHalf.size() > upperHalf.size()){
            return lowerHalf.peek();
        }
        else if(upperHalf.size() > lowerHalf.size()){
            return upperHalf.peek();
        }
        else {
            return ((double)lowerHalf.peek() + upperHalf.peek()) / 2;
        }
    }

    private static void calculateRunningMedian(int[] numbers) {
        PriorityQueue<Integer> lowerHalf = new PriorityQueue<Integer>(numbers.length,
                                                                      new Comparator<Integer>() {
                                                                         public int compare(Integer a, Integer b) {
                                                                             return -1 * a.compareTo(b);
                                                                         }
                                                                     });
        PriorityQueue<Integer> upperHalf = new PriorityQueue<Integer>(numbers.length);        
    
        for(int i : numbers) {
            addNumber(i, lowerHalf, upperHalf);
            balanceHeaps(lowerHalf, upperHalf);
            double median = calculateMedian(lowerHalf, upperHalf);
            System.out.println(format.format(median));
        }  
    }


    //private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("RunningMedian.txt");
        final Scanner scanner = new Scanner(file);
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            int aItem = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            a[i] = aItem;
        }
        long startTime = System.nanoTime();
        //calculateRunningMedianImperative(a, new ArrayList<Integer>(0));
        //calculateRunningMedianPriorityQueueAsHeap(a, new PriorityQueue<Integer>(), 0);
        calculateRunningMedian(a);
        
        long endTime = System.nanoTime();

        long duration = (endTime - startTime)/ 1000000;
        System.out.println("Took miliseconds");
        System.out.println(duration);
        scanner.close();
    }
}
