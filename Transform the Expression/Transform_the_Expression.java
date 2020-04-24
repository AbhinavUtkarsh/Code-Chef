import java.util.*;

class Transform_of_the_Expression {

    Scanner sc = new Scanner(System.in);

    static int get_precedence(char i) {

        switch (i) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;

        default:
            return -1;
        }

    }

    public static void main(String args[]) {
        Transform_of_the_Expression TOTE = new Transform_of_the_Expression();
    }
}