// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Calculadora Avanzada en Java

import java.util.Scanner;

public class CalculadoraAvanzada {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Calculadora Avanzada");
        System.out.println("Seleccione una operación:");
        System.out.println("1. Exponenciación");
        System.out.println("2. Raíz Cuadrada");
        System.out.println("3. Seno");
        System.out.println("4. Coseno");
        System.out.println("5. Tangente");
        System.out.println("6. Salir");

        int opcion = scanner.nextInt();

        switch (opcion) {
            case 1:
                System.out.print("Ingrese la base: ");
                double base = scanner.nextDouble();
                System.out.print("Ingrese el exponente: ");
                double exponente = scanner.nextDouble();
                System.out.println("Resultado: " + Math.pow(base, exponente));
                break;
            case 2:
                System.out.print("Ingrese el número: ");
                double numero = scanner.nextDouble();
                System.out.println("Resultado: " + Math.sqrt(numero));
                break;
            case 3:
                System.out.print("Ingrese el ángulo en grados: ");
                double anguloSeno = Math.toRadians(scanner.nextDouble());
                System.out.println("Resultado: " + Math.sin(anguloSeno));
                break;
            case 4:
                System.out.print("Ingrese el ángulo en grados: ");
                double anguloCoseno = Math.toRadians(scanner.nextDouble());
                System.out.println("Resultado: " + Math.cos(anguloCoseno));
                break;
            case 5:
                System.out.print("Ingrese el ángulo en grados: ");
                double anguloTangente = Math.toRadians(scanner.nextDouble());
                System.out.println("Resultado: " + Math.tan(anguloTangente));
                break;
            case 6:
                System.out.println("Saliendo de la calculadora.");
                break;
            default:
                System.out.println("Opción no válida.");
                break;
        }

        scanner.close();
    }
}
