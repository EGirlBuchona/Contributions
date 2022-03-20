// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Sistema de Búsqueda Avanzada en Java

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Producto {
    String nombre;
    double precio;
    String categoria;

    Producto(String nombre, double precio, String categoria) {
        this.nombre = nombre;
        this.precio = precio;
        this.categoria = categoria;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Precio: $" + precio + ", Categoría: " + categoria;
    }
}

public class BusquedaAvanzada {

    private static List<Producto> inventario = new ArrayList<>();

    public static void main(String[] args) {
        inicializarInventario();
        menu();
    }

    private static void inicializarInventario() {
        inventario.add(new Producto("Laptop", 1200, "Electrónica"));
        inventario.add(new Producto("Cámara", 600, "Fotografía"));
        inventario.add(new Producto("Teléfono", 800, "Electrónica"));
        inventario.add(new Producto("Silla", 150, "Muebles"));
        inventario.add(new Producto("Mesa", 300, "Muebles"));
    }

    private static void menu() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nSistema de Búsqueda Avanzada");
            System.out.println("1. Búsqueda por nombre");
            System.out.println("2. Búsqueda por categoría");
            System.out.println("3. Búsqueda por rango de precio");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese el nombre o prefijo: ");
                    String nombre = scanner.nextLine();
                    buscarPorNombre(nombre);
                    break;
                case 2:
                    System.out.print("Ingrese la categoría: ");
                    String categoria = scanner.nextLine();
                    buscarPorCategoria(categoria);
                    break;
                case 3:
                    System.out.print("Ingrese el precio mínimo: ");
                    double precioMin = scanner.nextDouble();
                    System.out.print("Ingrese el precio máximo: ");
                    double precioMax = scanner.nextDouble();
                    buscarPorRangoPrecio(precioMin, precioMax);
                    break;
                case 4:
                    System.out.println("Saliendo del sistema.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opción no válida.");
            }
        }
    }

    private static void buscarPorNombre(String nombre) {
        System.out.println("\nResultados de búsqueda por nombre:");
        for (Producto producto : inventario) {
            if (producto.nombre.toLowerCase().startsWith(nombre.toLowerCase())) {
                System.out.println(producto);
            }
        }
    }

    private static void buscarPorCategoria(String categoria) {
        System.out.println("\nResultados de búsqueda por categoría:");
        for (Producto producto : inventario) {
            if (producto.categoria.equalsIgnoreCase(categoria)) {
                System.out.println(producto);
            }
        }
    }

    private static void buscarPorRangoPrecio(double precioMin, double precioMax) {
        System.out.println("\nResultados de búsqueda por rango de precio:");
        for (Producto producto : inventario) {
            if (producto.precio >= precioMin && producto.precio <= precioMax) {
                System.out.println(producto);
            }
        }
    }
}
