// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Búsqueda Ternaria

public class BusquedaTernaria {

    public static int busquedaTernaria(int[] arr, int izquierda, int derecha, int objetivo) {
        if (derecha >= izquierda) {
            int tercio1 = izquierda + (derecha - izquierda) / 3;
            int tercio2 = derecha - (derecha - izquierda) / 3;

            if (arr[tercio1] == objetivo) {
                return tercio1;
            }
            if (arr[tercio2] == objetivo) {
                return tercio2;
            }
            if (objetivo < arr[tercio1]) {
                return busquedaTernaria(arr, izquierda, tercio1 - 1, objetivo);
            } else if (objetivo > arr[tercio2]) {
                return busquedaTernaria(arr, tercio2 + 1, derecha, objetivo);
            } else {
                return busquedaTernaria(arr, tercio1 + 1, tercio2 - 1, objetivo);
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int objetivo = 5;
        int resultado = busquedaTernaria(arr, 0, arr.length - 1, objetivo);

        if (resultado != -1) {
            System.out.println("El elemento " + objetivo + " se encuentra en el índice: " + resultado);
        } else {
            System.out.println("El elemento " + objetivo + " no se encuentra en el array.");
        }
    }
}
