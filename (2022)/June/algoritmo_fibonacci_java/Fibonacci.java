// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Algoritmo de Fibonacci en Java

import java.util.Scanner;

public class Fibonacci {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Bienvenido al Algoritmo de Fibonacci");
        System.out.print("Ingrese el número de términos de Fibonacci que desea calcular: ");
        int n = scanner.nextInt();

        System.out.println("\nFibonacci (Iterativo):");
        for (int i = 0; i < n; i++) {
            System.out.print(fibonacciIterativo(i) + " ");
        }

        System.out.println("\n\nFibonacci (Recursivo):");
        for (int i = 0; i < n; i++) {
            System.out.print(fibonacciRecursivo(i) + " ");
        }
    }

    public static int fibonacciIterativo(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1, c = 0;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    public static int fibonacciRecursivo(int n) {
        if (n <= 1) return n;
        return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2);
    }
}
