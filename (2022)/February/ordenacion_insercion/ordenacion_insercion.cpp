// Gustavo Cocone Zavaleta | GitHub: @EgirlBuchona | © 2022
// Proyecto: Implementación de Ordenación por Inserción en C++

#include <iostream>
using namespace std;

void ordenacionPorInsercion(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int clave = arr[i];
        int j = i - 1;

        // Mueve los elementos de arr[0..i-1] que son mayores que la clave
        // a una posición adelante de su posición actual
        while (j >= 0 && arr[j] > clave)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = clave;
    }
}

void imprimirArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Array original: ";
    imprimirArray(arr, n);

    ordenacionPorInsercion(arr, n);

    cout << "Array ordenado: ";
    imprimirArray(arr, n);

    return 0;
}
