import java.util.*;

class Mahasena {
    Scanner sc = new Scanner(System.in);

    Mahasena() {
        int total_soldiers = sc.nextInt(); // taking in the size
        int[] weapon = new int[total_soldiers];
        for (int i = 0; i < total_soldiers; i++) {
            weapon[i] = sc.nextInt(); // taking in the array
        }
        int counter_even = 0; // counter variables for our even or odd weapons
        int counter_odd = 0;
        for (int i = 0; i < total_soldiers; i++) {
            if (weapon[i] % 2 == 0) // even number detection logic
                counter_even++;
            else
                counter_odd++; // incrimination of respective counters
        }
        if (counter_even > counter_odd) // result displaying
            System.out.println("READY FOR BATTLE");
        else
            System.out.println("NOT READY");
    }

    public static void main(String args[]) {
        Mahasena M = new Mahasena();
    }
}