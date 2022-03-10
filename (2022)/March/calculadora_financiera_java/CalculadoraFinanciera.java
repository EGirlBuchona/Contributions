// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Calculadora Financiera en Java

import java.util.Scanner;

public class CalculadoraFinanciera {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Calculadora Financiera");
        System.out.println("1. Cálculo de Interés Compuesto");
        System.out.println("2. Cálculo de Pago de Préstamo");
        System.out.print("Seleccione una opción: ");
        int opcion = scanner.nextInt();

        switch (opcion) {
            case 1:
                calcularInteresCompuesto(scanner);
                break;
            case 2:
                calcularPagoPrestamo(scanner);
                break;
            default:
                System.out.println("Opción no válida.");
        }
        scanner.close();
    }

    private static void calcularInteresCompuesto(Scanner scanner) {
        System.out.print("Ingrese el capital inicial: ");
        double capital = scanner.nextDouble();
        System.out.print("Ingrese la tasa de interés anual (en %): ");
        double tasa = scanner.nextDouble() / 100;
        System.out.print("Ingrese el número de años: ");
        int años = scanner.nextInt();

        double montoFinal = capital * Math.pow(1 + tasa, años);
        System.out.printf("El monto final después de %d años es: %.2f%n", años, montoFinal);
    }

    private static void calcularPagoPrestamo(Scanner scanner) {
        System.out.print("Ingrese el monto del préstamo: ");
        double prestamo = scanner.nextDouble();
        System.out.print("Ingrese la tasa de interés anual (en %): ");
        double tasa = scanner.nextDouble() / 100 / 12;  // tasa mensual
        System.out.print("Ingrese el número de pagos: ");
        int pagos = scanner.nextInt();

        double pagoMensual = (prestamo * tasa) / (1 - Math.pow(1 + tasa, -pagos));
        System.out.printf("El pago mensual es: %.2f%n", pagoMensual);
    }
}
