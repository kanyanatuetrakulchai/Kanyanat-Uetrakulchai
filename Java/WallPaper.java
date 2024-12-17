import java.util.Scanner;

public class WallPaper {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // Task 1: Print out 3 popular styles
        /**************** YOUR CODE HERE (Task 1) *******************/
        System.out.println("=== Welcome to Customized Wallpaper System ===");
        System.out.println("We have 3 popular styles here:");
        System.out.println("=== Style 1 ===");
        int total = 0;
        // put your code here
        int i, j, n = 5;
        for (i = 1; i <= n; i++) {// row
            for (j = 1; j <= i; j++) { // col
                System.out.print(j + " ");
            }
            System.out.println();
        }
        System.out.println("=== Style 2 ===");
        // put your code here
        for (i = 1; i <= n; i++) {// row
            for (j = 1; j <= n; j++) {
                if (j >= i) {
                    System.out.print("_");
                } else {
                    System.out.print(" ");
                }
                System.out.print(" ");
            }
            System.out.println();
        }

        System.out.println("=== Style 3 ===");
        /**************** YOUR CODE HERE (Task 1) *******************/
        for (i = 1; i <= n; i++) {// row
            for (j = 1; j <= n; j++) { // col
                if (j <= i) {
                    System.out.print(j);
                } else {
                    System.out.print("_");
                }
                System.out.print(" ");

            }
            System.out.println();
        }
        /************************************************************/

        // Task 2: Get the size, style and symbol from users and print the output

        boolean stopProgram = false;
        while (!stopProgram) {

            System.out.print("Please choose your style: ");
            int style = in.nextInt();
            System.out.print("Size: ");
            int size = in.nextInt();
            System.out.print("Symbol: ");
            char symbol = in.next().charAt(0);
            /**************** YOUR CODE HERE (Task 2) *******************/
            switch (style) {
                case 1:
                    total += 100;
                    for (i = 1; i <= size; i++) {// row
                        for (j = 1; j <= i; j++) { // col
                            System.out.print(j + " ");
                        }
                        System.out.println();
                    }
                    break;

                case 2:
                    total += 200;
                    for (i = 1; i <= size; i++) {// row
                        for (j = 1; j <= size; j++) {
                            if (j >= i) {
                                System.out.print(symbol);
                            } else {
                                System.out.print(" ");
                            }
                            System.out.print(" ");
                        }
                        System.out.println();
                    }
                    break;

                case 3:
                    total += 300;
                    for (i = 1; i <= size; i++) {// row
                        for (j = 1; j <= size; j++) { // col
                            if (j <= i) {
                                System.out.print(j);
                            } else {
                                System.out.print(symbol);
                            }
                            System.out.print(" ");
                        }
                        System.out.println();
                    }
                    break;

                case -1:
                    System.out.println("Bye");
                    stopProgram = true;
                    break;
            }

        }
        /************************************************************/
        // }

        // Task 3: Bill the user
        /**************** YOUR CODE HERE (Task 3) *******************/
        System.out.println("Total Bill: " + total);
        in.close();
    }

}