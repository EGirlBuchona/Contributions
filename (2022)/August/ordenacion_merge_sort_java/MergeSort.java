// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Ordenación Merge Sort en Java

public class MergeSort {

    // Método principal de Merge Sort
    public static void mergeSort(int[] array) {
        if (array.length > 1) {
            int mid = array.length / 2;

            // Dividir el array en dos mitades
            int[] left = new int[mid];
            int[] right = new int[array.length - mid];

            System.arraycopy(array, 0, left, 0, mid);
            System.arraycopy(array, mid, right, 0, array.length - mid);

            // Ordenar cada mitad recursivamente
            mergeSort(left);
            mergeSort(right);

            // Combinar las mitades ordenadas
            merge(array, left, right);
        }
    }

    // Método para combinar dos subarrays ordenados
    private static void merge(int[] array, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                array[k++] = left[i++];
            } else {
                array[k++] = right[j++];
            }
        }

        // Copiar los elementos restantes
        while (i < left.length) {
            array[k++] = left[i++];
        }
        while (j < right.length) {
            array[k++] = right[j++];
        }
    }

    public static void main(String[] args) {
        int[] array = {38, 27, 43, 3, 9, 82, 10};
        System.out.println("Array original:");
        for (int num : array) {
            System.out.print(num + " ");
        }

        mergeSort(array);

        System.out.println("\n\nArray ordenado:");
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}
