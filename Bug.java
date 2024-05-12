public class Bug {
    public static void main(String[] args) {
        int x = 5;
        int y = 0;

        System.out.println("Division: " + (x / y)); // Bug: Division by zero

        String str = null;
        System.out.println("String Length: " + str.length()); // Bug: Null pointer exception

        int[] numbers = {1, 2, 3};
        System.out.println("Fourth Element: " + numbers[3]); // Bug: Array index out of bounds

        // Missing closing curly brace for the main method
