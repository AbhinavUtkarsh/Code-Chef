import java.util.*;

class Cutting_Recipes {

    Scanner sc = new Scanner(System.in);

    Cutting_Recipes() {

        int test = sc.nextInt(); // taking in the test cases
        while (test != 0) {
            int size = sc.nextInt(); // taking in the array size
            int[] array = new int[size];
            for (int i = 0; i < size; i++) {
                array[i] = sc.nextInt(); // taking in the array itself
            }
            int initial = GCD(array[0], array[1]); // getting the initial GCD of 1st two elements
            for (int i = 0; i < size; i++) {
                initial = GCD(initial, array[i]); // iterating over the array with initial GCD to get the common GCD of
                                                  // all elements
            }
            for (int i = 0; i < size; i++) {
                System.out.print(array[i] / initial + " "); // displaying the minimum quality of each ingredient
                                                            // required in balanced ratio
            }
            System.out.println();
            test--;
        }
    }

    int GCD(int a, int b) { // Our GCD recursive function
        if (a == b) { // base condition, when the numbers get equal then the GCD would also be the
                      // number itself
            return a;
        } else if (a > b) { // Euclidean method to find GCD, subtract the larger number from the smaller
                            // until they become equal
            return GCD(a - b, b); // when a>b
        } else {
            return GCD(a, b - a); // when b>a
        }
    }

    public static void main(String args[]) {
        Cutting_Recipes CR = new Cutting_Recipes();

    }
}