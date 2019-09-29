import java.util.*;

class The_Block_Game {

    The_Block_Game() {
        Scanner sc = new Scanner(System.in);
        int test = sc.nextInt(); // taking in the number of test cases
        while (test != 0) {
            int number = sc.nextInt(); // taking in the number
            int copy = number, dummy = 0; // creating a copy for later comparison and a dummy for reversing it
            while (number != 0) {
                dummy = dummy * 10 + (number % 10); // the palindrome code
                number = number / 10; // moving on to next digit from right
            }
            if (dummy == copy) { // comparing the number with the copy that we created earlier
                System.out.println("wins"); // printing out the result
            } else {
                System.out.println("losses");
            }
            test--;
        }
    }

    public static void main(String args[]) {
        The_Block_Game TBG = new The_Block_Game();
    }
}
