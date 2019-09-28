import java.util.*;

class Ambiguous_Permutations {

    Scanner sc = new Scanner(System.in);

    Ambiguous_Permutations() {

        int n = 1; // Using it as a flag variable to terminate when 0
        while (n != 0) {
            n = sc.nextInt(); // taking the size in
            if (n == 0) // Just as above,used to terminate the code when 0
                break;

            int permutation[] = new int[n + 1];
            for (int i = 1; i <= n; i++) { // taking in the numbers
                permutation[i] = sc.nextInt();
            }
            int copy[] = new int[n + 1];
            for (int i = 1; i <= n; i++) { // using a dummy array to place the inverse
                copy[permutation[i]] = i;
            }

            int flag = 1;

            for (int i = 1; i <= n; i++) { // checking if anything has changed and setting the flag if yes
                if (permutation[i] != copy[i]) {
                    flag = 0;
                }
            }
            if (flag == 0) // just printing out the result on the basis of flag value
                System.out.println("not ambiguous");
            else
                System.out.println("ambiguous");

        }

    }

    public static void main(String args[]) {
        Ambiguous_Permutations AP = new Ambiguous_Permutations();

    }
}