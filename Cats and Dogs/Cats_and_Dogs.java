import java.util.*;

class Cats_and_Dogs {

    Scanner sc = new Scanner(System.in);

    Cats_and_Dogs() {
        int test = sc.nextInt(); // getting in the number of test cases
        while (test != 0) {
            int C = sc.nextInt(); // getting in the number of cats
            int D = sc.nextInt(); // getting in the number of dogs
            int L = sc.nextInt(); // getting in the number of legs seen
            int minimum_to_be_reported = 0; // our conditional variable
            if (C > 2 * D) { // when the cats outnumber the number of seats
                minimum_to_be_reported = (C - D) * 4; // here the variable will hold the minimum number of legs to be
                                                      // reported when
                // we don't have enough occupancy

            } else { // when there are enough seats for the cats to get their ride
                minimum_to_be_reported = D * 4; // here the variable will hold the minimum number of legs to be reported
                // for the farmer to be right when we have enough occupancy
            }
            if (L % 4 == 0 && (C + D) * 4 >= L && minimum_to_be_reported <= L) {
                // the number of legs will always be a multiple of 4,
                // and can't exceed when all the animals are standing
                // and obviously would always be less than the above minimum_to_be_reported
                // variable.
                System.out.println("yes"); // displaying the result when positive :remember its only a possibility.
            } else {
                System.out.println("no"); // or when negative.
            }

            test--; // decrementing the test loop counter
        }
    }

    public static void main(String args[]) {
        Cats_and_Dogs CAD = new Cats_and_Dogs();
    }
}