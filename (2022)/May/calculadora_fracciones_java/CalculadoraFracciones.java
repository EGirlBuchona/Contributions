// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Calculadora de Fracciones en Java

import java.util.Scanner;

class Fraccion {
    int numerador;
    int denominador;

    public Fraccion(int numerador, int denominador) {
        this.numerador = numerador;
        this.denominador = denominador;
        simplificar();
    }

    public Fraccion sumar(Fraccion otra) {
        int nuevoNumerador = this.numerador * otra.denominador + otra.numerador * this.denominador;
        int nuevoDenominador = this.denominador * otra.denominador;
        return new Fraccion(nuevoNumerador, nuevoDenominador);
    }

    public Fraccion restar(Fraccion otra) {
        int nuevoNumerador = this.numerador * otra.denominador - otra.numerador * this.denominador;
        int nuevoDenominador = this.denominador * otra.denominador;
        return new Fraccion(nuevoNumerador, nuevoDenominador);
    }

    public Fraccion multiplicar(Fraccion otra) {
        return new Fraccion(this.numerador * otra.numerador, this.denominador * otra.denominador);
    }

    public Fraccion dividir(Fraccion otra) {
        return new Fraccion(this.numerador * otra.denominador, this.denominador * otra.numerador);
    }

    private void simplificar() {
        int gcd = mcd(numerador, denominador);
        numerador /= gcd;
        denominador /= gcd;
    }

    private int mcd(int a, int b) {
        return b == 0 ? a : mcd(b, a % b);
    }

    @Override
    public String toString() {
        return numerador + "/" + denominador;
    }
}

public class CalculadoraFracciones {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Calculadora de Fracciones");
        System.out.print("Ingrese el numerador de la primera fracción: ");
        int num1 = scanner.nextInt();
        System.out.print("Ingrese el denominador de la primera fracción: ");
        int den1 = scanner.nextInt();
        Fraccion fraccion1 = new Fraccion(num1, den1);

        System.out.print("Ingrese el numerador de la segunda fracción: ");
        int num2 = scanner.nextInt();
        System.out.print("Ingrese el denominador de la segunda fracción: ");
        int den2 = scanner.nextInt();
        Fraccion fraccion2 = new Fraccion(num2, den2);

        System.out.println("Seleccione una operación: ");
        System.out.println("1. Suma");
        System.out.println("2. Resta");
        System.out.println("3. Multiplicación");
        System.out.println("4. División");
        int opcion = scanner.nextInt();

        Fraccion resultado = null;
        switch (opcion) {
            case 1 -> resultado = fraccion1.sumar(fraccion2);
            case 2 -> resultado = fraccion1.restar(fraccion2);
            case 3 -> resultado = fraccion1.multiplicar(fraccion2);
            case 4 -> resultado = fraccion1.dividir(fraccion2);
            default -> System.out.println("Opción inválida.");
        }

        if (resultado != null) {
            System.out.println("Resultado: " + resultado);
        }

        scanner.close();
    }
}
