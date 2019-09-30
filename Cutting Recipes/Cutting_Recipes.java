import java.util.*;

class Cutting_Recipes {

    Scanner sc = new Scanner(System.in);

    Cutting_Recipes() {

        int test = sc.nextInt();
        while (test != 0) {
            int size = sc.nextInt();
            int[] array = new int[size];
            for (int i = 0; i < size; i++) {
                array[i] = sc.nextInt();
            }
            int initial = GCD(array[0], array[1]);
            for (int i = 0; i < size; i++) {
                initial = GCD(initial, array[i]);
            }
            for (int i = 0; i < size; i++) {
                System.out.print(array[i] / initial + " ");
            }
            System.out.println();
            test--;
        }
    }

    int GCD(int a, int b) {
        if (a == b) {
            return a;
        } else if (a > b) {
            return GCD(a - b, b);
        } else {
            return GCD(a, b - a);
        }
    }

    public static void main(String args[]) {
        Cutting_Recipes CR = new Cutting_Recipes();

    }
}