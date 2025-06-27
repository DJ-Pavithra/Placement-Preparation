import java.util.Scanner;
import java.util.ArrayList;
public class Array{
    public static void main(String[] args){
       Scanner sc=new Scanner(System.in);
       int[] arr=new int[5];

       for(int i=0;i<arr.length;i++){
        arr[i]=sc.nextInt();
       }

       System.out.println(java.util.Arrays.toString(arr));
       
       ArrayList<Integer> list = new ArrayList<>();
       System.out.println("Enter 5 numbers:");
        for (int i = 0; i < 5; i++) {
            list.add(sc.nextInt());
        }

        System.out.println("List: " + list);


    }
}