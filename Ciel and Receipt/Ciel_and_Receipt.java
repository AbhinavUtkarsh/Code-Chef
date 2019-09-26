import java.util.Scanner;

class Ciel_and_Receipt {

    Scanner sc = new Scanner(System.in);
    int test = sc.nextInt();// input for test cases

    Ciel_and_Receipt() {

        int counter = 0;

        while (test > 0) {
            int p = sc.nextInt(); // input for positive number
            int binary[] = new int[12]; // binary array
            int i = 0;
            counter = 0;

            if (p > 2048) { // when number greater than the menu item
                counter = p / 2048;
                p = (int) (p - 2048 * counter); // changing the number
            }
            while (p > 0) { // binary conversation
                binary[i] = p % 2;
                p = p / 2;
                i++;
            }
            for (i = 0; i < binary.length; i++) { // bit's counting from binary array
                if (binary[i] == 1)
                    counter++;
            }
            System.out.println(counter); // printing final result
            test--;
        }

    }

    public static void main(String args[]) {
        Ciel_and_Receipt CR = new Ciel_and_Receipt();

    }
}