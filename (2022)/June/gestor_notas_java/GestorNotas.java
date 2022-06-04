// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Gestor de Notas en Java

import java.util.ArrayList;
import java.util.Scanner;

public class GestorNotas {
    private static ArrayList<String> notas = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean continuar = true;

        while (continuar) {
            System.out.println("\nGestor de Notas");
            System.out.println("1. Agregar nota");
            System.out.println("2. Eliminar nota");
            System.out.println("3. Buscar nota");
            System.out.println("4. Mostrar todas las notas");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine();  // Consume la nueva línea

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese la nota a agregar: ");
                    String nota = scanner.nextLine();
                    agregarNota(nota);
                    break;
                case 2:
                    System.out.print("Ingrese el índice de la nota a eliminar: ");
                    int indiceEliminar = scanner.nextInt();
                    eliminarNota(indiceEliminar);
                    break;
                case 3:
                    System.out.print("Ingrese una palabra clave para buscar: ");
                    String palabraClave = scanner.nextLine();
                    buscarNota(palabraClave);
                    break;
                case 4:
                    mostrarNotas();
                    break;
                case 5:
                    continuar = false;
                    System.out.println("Saliendo del gestor de notas.");
                    break;
                default:
                    System.out.println("Opción no válida.");
                    break;
            }
        }
        scanner.close();
    }

    public static void agregarNota(String nota) {
        notas.add(nota);
        System.out.println("Nota agregada exitosamente.");
    }

    public static void eliminarNota(int indice) {
        if (indice >= 0 && indice < notas.size()) {
            notas.remove(indice);
            System.out.println("Nota eliminada exitosamente.");
        } else {
            System.out.println("Índice no válido.");
        }
    }

    public static void buscarNota(String palabraClave) {
        System.out.println("Resultados de búsqueda:");
        for (int i = 0; i < notas.size(); i++) {
            if (notas.get(i).contains(palabraClave)) {
                System.out.println("Índice: " + i + " - Nota: " + notas.get(i));
            }
        }
    }

    public static void mostrarNotas() {
        System.out.println("Lista de notas:");
        for (int i = 0; i < notas.size(); i++) {
            System.out.println("Índice: " + i + " - Nota: " + notas.get(i));
        }
    }
}
