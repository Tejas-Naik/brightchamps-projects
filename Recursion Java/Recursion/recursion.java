//find factorial of a number
import java.util.Scanner;
public class MyClass {
    public static void main(String args[]) {
        Scanner sc=new Scanner(System.in);
	    System.out.println("enter the number ");
	    int num=sc.nextInt();
     
       System.out.println("Factorial of "+num+ " is "+factorial(num));
            
    }
    
    public static Integer factorial(int number) {
        if (number == 1) {
            return 1;
        } 
        else {
            return number*factorial(number-1);
        }
    }
}