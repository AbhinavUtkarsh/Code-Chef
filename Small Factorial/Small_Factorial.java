import java.util.*;

class Small_Factorial {

    Scanner sc = new Scanner(System.in);
    int test = sc.nextInt();// taking the input for test cases

    Small_Factorial() { // our constructor
        while (test > 0) {
            int n = sc.nextInt(); // Input for the number
            int fact = 1;
            int i = 1;
            while (i <= n) { // calculating the factorial
                fact *= i;
                i++;
            }
            System.out.println(fact); // displaying the result
            test--;
        }
    }

    public static void main(String args[]) {
        Small_Factorial SF = new Small_Factorial();

    }
}