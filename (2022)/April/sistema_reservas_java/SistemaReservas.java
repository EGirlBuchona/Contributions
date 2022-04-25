// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Sistema de Reservas de Asientos en Java

import java.util.Scanner;

public class SistemaReservas {
    private static final int FILAS = 5;
    private static final int COLUMNAS = 5;
    private static boolean[][] asientos = new boolean[FILAS][COLUMNAS];
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int opcion;
        do {
            System.out.println("\nSistema de Reservas de Asientos");
            System.out.println("1. Mostrar asientos");
            System.out.println("2. Reservar asiento");
            System.out.println("3. Liberar asiento");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    mostrarAsientos();
                    break;
                case 2:
                    reservarAsiento();
                    break;
                case 3:
                    liberarAsiento();
                    break;
                case 4:
                    System.out.println("Gracias por utilizar el sistema de reservas.");
                    break;
                default:
                    System.out.println("Opción inválida. Intente de nuevo.");
            }
        } while (opcion != 4);
    }

    private static void mostrarAsientos() {
        System.out.println("\nEstado de los asientos (O: libre, X: reservado):");
        for (int i = 0; i < FILAS; i++) {
            for (int j = 0; j < COLUMNAS; j++) {
                System.out.print(asientos[i][j] ? "X " : "O ");
            }
            System.out.println();
        }
    }

    private static void reservarAsiento() {
        System.out.print("Ingrese la fila del asiento (1-5): ");
        int fila = scanner.nextInt() - 1;
        System.out.print("Ingrese la columna del asiento (1-5): ");
        int columna = scanner.nextInt() - 1;

        if (fila >= 0 && fila < FILAS && columna >= 0 && columna < COLUMNAS) {
            if (!asientos[fila][columna]) {
                asientos[fila][columna] = true;
                System.out.println("Asiento reservado exitosamente.");
            } else {
                System.out.println("El asiento ya está reservado.");
            }
        } else {
            System.out.println("Asiento inválido. Intente de nuevo.");
        }
    }

    private static void liberarAsiento() {
        System.out.print("Ingrese la fila del asiento (1-5): ");
        int fila = scanner.nextInt() - 1;
        System.out.print("Ingrese la columna del asiento (1-5): ");
        int columna = scanner.nextInt() - 1;

        if (fila >= 0 && fila < FILAS && columna >= 0 && columna < COLUMNAS) {
            if (asientos[fila][columna]) {
                asientos[fila][columna] = false;
                System.out.println("Asiento liberado exitosamente.");
            } else {
                System.out.println("El asiento ya estaba libre.");
            }
        } else {
            System.out.println("Asiento inválido. Intente de nuevo.");
        }
    }
}
