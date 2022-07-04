// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Gestor de Clientes en Java

import java.util.ArrayList;
import java.util.Scanner;

class Cliente {
    int id;
    String nombre;
    String email;

    Cliente(int id, String nombre, String email) {
        this.id = id;
        this.nombre = nombre;
        this.email = email;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Nombre: " + nombre + ", Email: " + email;
    }
}

public class GestorClientes {
    static ArrayList<Cliente> clientes = new ArrayList<>();
    static int nextId = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\nGestor de Clientes");
            System.out.println("1. Agregar Cliente");
            System.out.println("2. Listar Clientes");
            System.out.println("3. Actualizar Cliente");
            System.out.println("4. Eliminar Cliente");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea

            switch (opcion) {
                case 1 -> agregarCliente(scanner);
                case 2 -> listarClientes();
                case 3 -> actualizarCliente(scanner);
                case 4 -> eliminarCliente(scanner);
                case 5 -> System.out.println("Saliendo del Gestor de Clientes.");
                default -> System.out.println("Opción no válida. Intente de nuevo.");
            }
        } while (opcion != 5);

        scanner.close();
    }

    public static void agregarCliente(Scanner scanner) {
        System.out.print("Nombre del cliente: ");
        String nombre = scanner.nextLine();
        System.out.print("Email del cliente: ");
        String email = scanner.nextLine();

        clientes.add(new Cliente(nextId++, nombre, email));
        System.out.println("Cliente agregado exitosamente.");
    }

    public static void listarClientes() {
        if (clientes.isEmpty()) {
            System.out.println("No hay clientes registrados.");
        } else {
            System.out.println("\nLista de Clientes:");
            for (Cliente cliente : clientes) {
                System.out.println(cliente);
            }
        }
    }

    public static void actualizarCliente(Scanner scanner) {
        System.out.print("Ingrese el ID del cliente a actualizar: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consumir el salto de línea

        Cliente cliente = buscarClientePorId(id);
        if (cliente != null) {
            System.out.print("Nuevo nombre (actual: " + cliente.nombre + "): ");
            cliente.nombre = scanner.nextLine();
            System.out.print("Nuevo email (actual: " + cliente.email + "): ");
            cliente.email = scanner.nextLine();
            System.out.println("Cliente actualizado exitosamente.");
        } else {
            System.out.println("Cliente no encontrado.");
        }
    }

    public static void eliminarCliente(Scanner scanner) {
        System.out.print("Ingrese el ID del cliente a eliminar: ");
        int id = scanner.nextInt();

        Cliente cliente = buscarClientePorId(id);
        if (cliente != null) {
            clientes.remove(cliente);
            System.out.println("Cliente eliminado exitosamente.");
        } else {
            System.out.println("Cliente no encontrado.");
        }
    }

    public static Cliente buscarClientePorId(int id) {
        for (Cliente cliente : clientes) {
            if (cliente.id == id) {
                return cliente;
            }
        }
        return null;
    }
}
