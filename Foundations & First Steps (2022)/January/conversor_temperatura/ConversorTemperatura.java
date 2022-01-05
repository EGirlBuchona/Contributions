// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Conversor de Temperatura en Java

import java.util.Scanner;

public class ConversorTemperatura {

    public static void main(String[] args) {
        System.out.println("Conversor de Temperatura");
        System.out.println("Seleccione la conversión que desea realizar:");
        System.out.println("1. Celsius a Fahrenheit");
        System.out.println("2. Celsius a Kelvin");
        System.out.println("3. Fahrenheit a Celsius");
        System.out.println("4. Fahrenheit a Kelvin");
        System.out.println("5. Kelvin a Celsius");
        System.out.println("6. Kelvin a Fahrenheit");

        try (Scanner scanner = new Scanner(System.in)) {  // try-with-resources
            int opcion = scanner.nextInt();
            System.out.print("Ingrese la temperatura: ");
            double temperatura = scanner.nextDouble();
            double resultado = 0;

            switch (opcion) {
                case 1 ->
                    resultado = celsiusAFahrenheit(temperatura);
                case 2 ->
                    resultado = celsiusAKelvin(temperatura);
                case 3 ->
                    resultado = fahrenheitACelsius(temperatura);
                case 4 ->
                    resultado = fahrenheitAKelvin(temperatura);
                case 5 ->
                    resultado = kelvinACelsius(temperatura);
                case 6 ->
                    resultado = kelvinAFahrenheit(temperatura);
                default ->
                    System.out.println("Opción no válida.");
            }

            if (opcion >= 1 && opcion <= 6) {
                System.out.println("Resultado: " + resultado);
            }
        } // El recurso Scanner se cierra automáticamente aquí
    }

    public static double celsiusAFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }

    public static double celsiusAKelvin(double celsius) {
        return celsius + 273.15;
    }

    public static double fahrenheitACelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    public static double fahrenheitAKelvin(double fahrenheit) {
        return (fahrenheit + 459.67) * 5 / 9;
    }

    public static double kelvinACelsius(double kelvin) {
        return kelvin - 273.15;
    }

    public static double kelvinAFahrenheit(double kelvin) {
        return (kelvin * 9 / 5) - 459.67;
    }
}
